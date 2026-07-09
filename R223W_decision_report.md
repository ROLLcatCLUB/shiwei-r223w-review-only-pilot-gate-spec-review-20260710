# R223W decision report

stage_id: 1013R_R223W_REVIEW_ONLY_PILOT_GATE_SPEC  
status: PASS_LOCAL_REVIEW_ONLY_PILOT_GATE_SPEC  
decision: PASS_CONTINUE_TO_R223X_REVIEW_ONLY_PILOT_GATE_FIXTURE

## Summary

R223W defines the review-only pilot gate specification after R223W-P0 source-of-truth contract.

It does not create a visual page or teacher draft. It only specifies the gate shape that a future fixture may follow.

## Key rules locked

1. Teacher draft is document-style primary reading.
2. Teacher draft source must be canonical R223M/N/O manuscripts.
3. R223W cannot create or rewrite teacher draft body.
4. Review ledger defaults collapsed / summary-first.
5. Component trigger is metadata only, not executable.
6. v0.1 / v0.2 difference summary comes before detailed review.
7. Safety banner always states v0.2 is not published and no writeback occurs.

## Next allowed

```text
1013R_R223X_REVIEW_ONLY_PILOT_GATE_FIXTURE
```

R223X may only create a fixture following this gate spec. It still may not be a formal UI or R97B route.

## Still blocked

```text
R223M_STANDARD_V0_2 = NOT_PUBLISHED
FORMAL_UI = BLOCKED
R97B_ROUTE = BLOCKED
FRONTEND_BACKEND = BLOCKED
RUNTIME_PROVIDER_MODEL_PROMPT_DB = BLOCKED
LESSON_BODY_WRITEBACK = BLOCKED
R222D_COMPONENT_LIBRARY_CHANGE = BLOCKED
FORMAL_APPLY = BLOCKED
```

