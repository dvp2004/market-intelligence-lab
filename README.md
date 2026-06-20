# Market Intelligence Lab

A research-only, point-in-time market-intelligence platform for testing whether carefully defined information families improve risk-adjusted allocation research over transparent baselines.

`market-intelligence-lab` complements `market-strats-lab`. It does not replace or duplicate GMA portfolio construction, risk controls, tournament selection, paper-readiness, manual TradingView workflow, fill validation, reconciliation, broker adapters, or execution controls.

## Current status

**MI-0 complete; MI-1 active.** The repository contains research boundaries, market-data contracts, the fixed 22-ETF universe, corporate-action policy, availability-evidence policy, public-data policy, a pre-registered MI-2 research registry, and the MI-1 market-data refresh command.

It does not contain:

- macro ingestion or a macro registry;
- technical features;
- models, LLM calls, or portfolio simulation;
- broker/API code, credentials, order submission, or real-money functionality.

## Fixed repository boundary

```text
market-intelligence-lab
-> research-only data contracts, feature-family experiments, reports, shadow candidate packets

market-strats-lab
-> portfolio construction, risk limits, GMA tournament, paper-readiness,
   manual TradingView workflow, fill validation, reconciliation
```

Any future candidate export remains broker-neutral and must include:

```text
research_only = true
portfolio_influence = 0
```

No candidate packet may contain an order, target weight, broker instruction, credential, or authority to alter GMA.

## MI-1 scope

MI-1 is strictly market-data only: daily end-of-day ETF bars, immutable snapshot manifests, normalized Parquet, coverage reporting, and availability audits. Macro data begins no earlier than MI-3.

## MI-1 market-data refresh

The MI-1 refresh command writes only to ignored local research paths under `data/private/mi1/` and `reports/mi1/`. The optional `--end` date is inclusive. Omit it to let the source adapter request the latest available daily history.

```powershell
python -m market_intelligence_lab.cli refresh-mi1-market-data `
  --universe-config configs/universe_mi1.yaml `
  --source-config configs/market_data_source_mi1.yaml `
  --data-root data/private/mi1 `
  --report-root reports/mi1 `
  --start 2000-01-01
```

Outputs:

- raw provider-response snapshots in `data/private/mi1/raw/`;
- `raw_snapshot_manifest.parquet` in `data/private/mi1/manifests/`;
- normalized `market_eod_bar.parquet` and `corporate_action_event.parquet`;
- `coverage_audit.parquet`, `availability_audit.parquet`, `decision_panel_availability_audit.parquet`, and `data_quality_event.parquet`;
- coverage and availability reports as Markdown and JSON in `reports/mi1/`.

The default yfinance source configuration is credential-free, uses `auto_adjust=False`, records corporate actions separately, and marks default availability evidence as `contractual_assumption`. This is not provider timestamp verification.

## Start here

- `docs/continuation_map.md`
- `docs/thesis_continuity_appendix.md`
- `docs/data_contracts.md`
- `docs/corporate_actions_and_price_policy.md`
- `docs/availability_evidence_policy.md`
- `docs/data_publication_policy.md`
- `configs/universe_mi1.yaml`
- `configs/mi2_research_registry.yaml`

## Public-repository rule

Code, contracts, manifests, synthetic fixtures, and permitted derived reports may be tracked. Credentials, licensed raw data, prohibited provider data, and non-permitted full copyrighted text must not be tracked.
