# Availability-Evidence Policy

Every dataset and normalized row must carry exactly one availability-evidence level.

| Evidence level | Meaning | Historical decision-panel eligibility |
| --- | --- | --- |
| `provider_timestamp_verified` | A source-provided publication or availability timestamp is stored and validated. | Eligible when the timestamp is no later than the decision cutoff. |
| `release_calendar_verified` | A documented release calendar plus the observed release rule supports availability timing. | Eligible when the derived timestamp is no later than the decision cutoff. |
| `contractual_assumption` | A documented, source-specific timing rule is used because a historical timestamp is unavailable. | Eligible only when explicitly approved in configuration and shown in reports. |
| `unverified` | Availability timing cannot be supported. | Never eligible for a historical decision panel. |

## Rules

1. Evidence level is mandatory in raw manifests, normalized records, availability audits, and reports.
2. A decision panel may use only verified rows or explicitly approved contractual assumptions.
3. `unverified` data may be stored for investigation but cannot be modeled or backtested as decision-time input.
4. Reports must show count and coverage by evidence level.
5. Contractual assumptions are not silently upgraded to verified status.