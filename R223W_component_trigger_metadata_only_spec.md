# R223W component trigger metadata-only spec

## Policy

Component trigger information must remain metadata only.

## Required visible label

```text
Component trigger metadata only. Not executable. Not added to component library.
```

## Allowed

- component status count
- component_id in full ledger
- status explanation for reviewers

## Blocked

- run component
- insert component
- apply to big screen
- add to component library
- teacher-facing component shelf
- classroom runtime execution

## Status handling

| status | gate behavior |
| --- | --- |
| already_registered | summary count + full ledger allowed |
| candidate_from_R222D_pool | summary count + full ledger allowed |
| new_surface_candidate | full ledger only |
| unregistered_do_not_execute | full ledger only with warning |

## Hold condition

Hold if component trigger status looks like an available teaching tool or classroom runtime feature.

