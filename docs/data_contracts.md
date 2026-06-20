# MI-1 Market-Data Contracts

MI-1 is market-data only. It must not fetch, register, normalize, or model macro data.

## `instrument_registry`

Required fields:

```text
instrument_id
symbol
asset_class
currency
exchange_calendar
source_symbol
eligible_from
active
registry_version
```

Rules:

- `instrument_id` is stable even when the public ticker changes.
- A ticker symbol is not a permanent identity.
- Universe membership is versioned and may not be silently edited.

## `raw_snapshot_manifest`

Required fields:

```text
snapshot_id
source_name
dataset_name
request_parameters
retrieved_at_utc
content_sha256
parser_version
raw_path
publication_permission
availability_evidence_level
```

Rules:

- Each normalized observation must trace to an immutable raw snapshot manifest.
- Raw source files remain local and ignored unless redistribution is explicitly permitted.

## `market_eod_bar`

Required fields:

```text
instrument_id
session_date
open_raw
high_raw
low_raw
close_raw
volume_raw
vendor_adjusted_close
adjustment_basis
available_at_utc
availability_evidence_level
availability_rule_id
retrieved_at_utc
snapshot_id
```

Rules:

- Raw OHLCV and adjusted values are separate fields.
- No historical decision panel may use a row whose `available_at_utc` is later than the decision cutoff.
- `unverified` rows are storage-eligible but decision-panel ineligible.

## `coverage_audit`

Required fields:

```text
run_id
instrument_id
first_observed_session
last_observed_session
eligible_sessions
missing_sessions
coverage_ratio
continuous_history_sessions
start_date_eligible
notes
```

Rules:

- The MI-2 research start date is determined by this audit, not assumed before data inspection.

## `availability_audit`

Required fields:

```text
decision_timestamp_utc
dataset_row_id
available_at_utc
availability_evidence_level
eligible
failure_reason
```

Rules:

- Every historical decision date receives a reproducible pass/fail decision.
- Reports must display evidence levels and cannot describe contractual or unverified timestamps as provider-verified facts.