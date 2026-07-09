# R223W review ledger collapsed summary spec

## Default state

The review ledger must be collapsed or summary-first by default.

```json
{
  "review_ledger_default_state": "collapsed_summary",
  "full_ledger_requires": "reviewer_action",
  "teacher_view_contains_full_ledger": false
}
```

## Summary-first fields

Only these may appear in default summary:

- event count
- primary pattern count
- component status count
- screen/sheet/evidence mapping count
- teacher confirmation count

## Full ledger

Full ledger may be opened only by reviewer action and must be labeled:

```text
Review ledger only. Not teacher manuscript. Not written back.
```

## Hold condition

Hold if the ledger appears as a second teacher draft, field wall or primary reading surface.

