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

## MI-2 technical baseline

The MI-2 command consumes accepted local MI-1 normalized outputs only. It does not refresh MI-1 data or use network access.

```powershell
python -m market_intelligence_lab.cli run-mi2-technical-baseline `
  --mi1-data-root data/private/mi1 `
  --mi2-data-root data/private/mi2 `
  --report-root reports/mi2
```

Outputs:

- `data/private/mi2/feature_panel.parquet`
- `data/private/mi2/target_panel.parquet`
- `data/private/mi2/walk_forward_predictions.parquet`
- `data/private/mi2/strategy_returns.parquet`
- `data/private/mi2/strategy_trades.parquet`
- `data/private/mi2/scoreboard.parquet`
- `reports/mi2/technical_baseline_scoreboard.md`
- `reports/mi2/technical_baseline_scoreboard.json`

MI-2 separates forecast evaluation from portfolio evaluation. Ridge forecast results are compared with zero-excess-return and persistence baselines; portfolio results cover the registered non-model baselines plus one fixed technical composite. No Ridge-driven portfolio strategy is created.

## MI-3 macro vintage forecast

The MI-3 command consumes local MI-1 and MI-2 outputs, then retrieves vintage-aware FRED/ALFRED observations using `FRED_API_KEY` from the active process environment. It does not load `.env` files and does not create a macro portfolio strategy.

```powershell
python -m market_intelligence_lab.cli run-mi3-macro-vintage-forecast `
  --mi1-data-root data/private/mi1 `
  --mi2-data-root data/private/mi2 `
  --mi3-data-root data/private/mi3 `
  --report-root reports/mi3
```

Outputs:

- `data/private/mi3/raw/`
- `data/private/mi3/manifests/macro_raw_snapshot_manifest.parquet`
- `data/private/mi3/normalized/macro_vintage_observation.parquet`
- `data/private/mi3/normalized/macro_asof_panel.parquet`
- `data/private/mi3/macro_feature_panel.parquet`
- `data/private/mi3/walk_forward_macro_predictions.parquet`
- `data/private/mi3/macro_forecast_scoreboard.parquet`
- `reports/mi3/macro_forecast_scoreboard.md`
- `reports/mi3/macro_forecast_scoreboard.json`

MI-3 is forecast evaluation only: zero excess return, persistence, technical-only Ridge, and technical-plus-macro Ridge are compared on the same macro-eligible observations.

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
