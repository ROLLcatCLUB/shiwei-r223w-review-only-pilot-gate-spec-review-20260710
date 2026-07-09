import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = [
    "R223W_review_only_pilot_gate_spec.md",
    "R223W_teacher_draft_primary_reading_shell_spec.md",
    "R223W_canonical_source_reference_contract.json",
    "R223W_review_ledger_collapsed_summary_spec.md",
    "R223W_v0_1_v0_2_difference_summary_spec.md",
    "R223W_component_trigger_metadata_only_spec.md",
    "R223W_safety_banner_and_flags_contract.json",
    "R223W_acceptance_and_hold_conditions.md",
    "R223W_decision_report.md",
    "README_FOR_GPT_REVIEW.md",
    "PACKAGE_MANIFEST.json",
]

CANONICAL_FILES = [
    "R223M_P4_P1_teacher_readable_process_v6.html",
    "R223N_P3_P1_teacher_manuscript_draft_v5.html",
    "R223O_P1_teacher_manuscript_draft_v2.html",
]

REQUIRED_DECISIONS = [
    "PASS_CONTINUE_TO_R223X_REVIEW_ONLY_PILOT_GATE_FIXTURE",
    "HOLD_FOR_R223W_GATE_SPEC_REDUCTION",
    "HOLD_FORMAL_V0_2_NOT_READY",
]

REQUIRED_PHRASES = [
    "review-only pilot gate",
    "teacher draft primary reading shell",
    "canonical teacher manuscripts",
    "collapsed / summary-first",
    "metadata only",
    "Not executable",
    "difference summary",
    "R223W must not create",
    "R223M_STANDARD_V0_2 = NOT_PUBLISHED",
    "FORMAL_UI = BLOCKED",
    "R97B_ROUTE = BLOCKED",
    "RUNTIME_PROVIDER_MODEL_PROMPT_DB = BLOCKED",
    "LESSON_BODY_WRITEBACK = BLOCKED",
]

BANNED_PHRASES = [
    "R223W_teacher_draft.html",
    "R223W_teacher_manuscript.html",
    "R223W_final_teacher_page.html",
    "R223M_STANDARD_V0_2 = PUBLISHED",
    "FORMAL_UI = ALLOWED",
    "R97B_ROUTE = ALLOWED",
    "teacher_confirmed=true",
    "formal_apply_allowed=true",
    "database_written=true",
    "lesson_body_written=true",
]

FALSE_BOUNDARIES = [
    "new_visual_page_created",
    "new_teacher_draft_created",
    "teacher_body_rewritten",
    "schema_v0_2_published",
    "formal_ui",
    "r97b_modified",
    "formal_route_added",
    "frontend_backend_modified",
    "runtime_connected",
    "provider_model_connected",
    "prompt_modified",
    "database_written",
    "lesson_body_written",
    "r222d_component_library_modified",
    "formal_apply",
]

def read_text(name):
    return (ROOT / name).read_text(encoding="utf-8")

def main():
    failures = []
    checks = 0

    for name in REQUIRED_FILES:
        checks += 1
        if not (ROOT / name).exists():
            failures.append(f"missing required file: {name}")

    combined = "\n".join(read_text(name) for name in REQUIRED_FILES if (ROOT / name).exists())

    for decision in REQUIRED_DECISIONS:
        checks += 1
        if decision not in combined:
            failures.append(f"missing decision output: {decision}")

    for phrase in REQUIRED_PHRASES:
        checks += 1
        if phrase not in combined:
            failures.append(f"missing required phrase: {phrase}")

    for phrase in BANNED_PHRASES:
        checks += 1
        if phrase in combined:
            failures.append(f"forbidden phrase present: {phrase}")

    source_path = ROOT / "R223W_canonical_source_reference_contract.json"
    if source_path.exists():
        source = json.loads(source_path.read_text(encoding="utf-8"))
        checks += 1
        if source.get("may_create_teacher_draft") is not False:
            failures.append("may_create_teacher_draft must be false")
        checks += 1
        if source.get("may_rewrite_teacher_body") is not False:
            failures.append("may_rewrite_teacher_body must be false")
        source_text = json.dumps(source, ensure_ascii=False)
        for name in CANONICAL_FILES:
            checks += 1
            if name not in source_text:
                failures.append(f"canonical source missing: {name}")

    safety_path = ROOT / "R223W_safety_banner_and_flags_contract.json"
    if safety_path.exists():
        safety = json.loads(safety_path.read_text(encoding="utf-8"))
        flags = safety.get("safety_flags", {})
        checks += 1
        if flags.get("review_only_pilot_gate") is not True:
            failures.append("review_only_pilot_gate must be true")
        for key in [
            "schema_v0_2_published",
            "teacher_confirmed",
            "formal_apply_allowed",
            "lesson_body_writeback",
            "may_create_teacher_draft",
            "may_rewrite_teacher_body",
            "r97b_modified",
            "formal_route_added",
            "frontend_backend_modified",
            "runtime_connected",
            "provider_model_connected",
            "prompt_modified",
            "database_written",
            "r222d_component_library_modified",
            "formal_apply",
        ]:
            checks += 1
            if flags.get(key) is not False:
                failures.append(f"safety flag must be false: {key}")

    manifest_path = ROOT / "PACKAGE_MANIFEST.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        checks += 1
        if manifest.get("stage_id") != "1013R_R223W_REVIEW_ONLY_PILOT_GATE_SPEC":
            failures.append("manifest stage_id mismatch")
        checks += 1
        if manifest.get("decision") != "PASS_CONTINUE_TO_R223X_REVIEW_ONLY_PILOT_GATE_FIXTURE":
            failures.append("manifest decision mismatch")
        boundaries = manifest.get("boundaries", {})
        for key in FALSE_BOUNDARIES:
            checks += 1
            if boundaries.get(key) is not False:
                failures.append(f"manifest boundary must be false: {key}")

    result = {
        "passed": not failures,
        "check_count": checks,
        "failed": len(failures),
        "failures": failures,
        "decision": "PASS_CONTINUE_TO_R223X_REVIEW_ONLY_PILOT_GATE_FIXTURE",
    }
    (ROOT / "validate_1013R_R223W_review_only_pilot_gate_spec_result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(0 if not failures else 1)

if __name__ == "__main__":
    main()

