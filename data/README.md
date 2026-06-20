# Data directory policy

- `raw/` contains immutable source snapshots and is ignored by Git.
- `normalized/` contains derived Parquet and is ignored by Git.
- `manifests/` may contain metadata-only manifests when publication is permitted.
- `private/` is reserved for local material that must never be tracked.
- Corporate-action and price-adjustment handling is governed by `docs/corporate_actions_and_price_policy.md`.