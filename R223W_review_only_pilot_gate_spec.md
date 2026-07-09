# R223W review-only pilot gate spec

stage_id: 1013R_R223W_REVIEW_ONLY_PILOT_GATE_SPEC  
status: gate_spec_only  
source: R223W-P0 artifact lineage contract

## 1. Purpose

R223W defines a review-only pilot gate for R223M classroom_event_standard v0.2 candidate.

This is not:

- a new teacher draft line
- a visual page implementation
- a formal route
- an R97B UI change
- a runtime/model/prompt/db integration

## 2. Source-of-truth rule

R223W must reference canonical teacher manuscripts only:

| sample | canonical teacher manuscript |
| --- | --- |
| M_stationery | R223M_P4_P1_teacher_readable_process_v6.html |
| N_paper_print | R223N_P3_P1_teacher_manuscript_draft_v5.html |
| O_color_collision | R223O_P1_teacher_manuscript_draft_v2.html |

R223W must not create:

```text
R223W_teacher_draft
R223W_teacher_manuscript
R223W_final_teacher_page
```

## 3. Gate structure

The review-only pilot gate may define these sections:

1. safety banner and status flags
2. canonical teacher manuscript reference
3. teacher draft primary reading shell
4. v0.1 / v0.2 short difference summary
5. collapsed review ledger summary
6. full review ledger on reviewer action
7. component trigger metadata-only summary
8. acceptance / hold decision checklist

## 4. Gate entry conditions

The gate may be entered only if:

- reviewer explicitly opens the review-only pilot gate
- fixture data is used
- teacher_confirmed=false
- formal_apply_allowed=false
- no lesson body writeback exists
- v0.2 remains not published

## 5. Gate exit decisions

Allowed decisions:

```text
PASS_CONTINUE_TO_R223X_REVIEW_ONLY_PILOT_GATE_FIXTURE
HOLD_FOR_R223W_GATE_SPEC_REDUCTION
HOLD_FORMAL_V0_2_NOT_READY
```

