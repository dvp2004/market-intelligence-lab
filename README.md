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

## MI-4 tree technical comparator

MI-4 is the final technical-model-family comparator. It consumes accepted local MI-2 outputs only and evaluates one fixed `RandomForestRegressor` technical model against the MI-2 forecast comparators. It does not refresh MI-1, run MI-2 or MI-3, use macro inputs, create a portfolio, or make trading recommendations.

```powershell
python -m market_intelligence_lab.cli run-mi4-tree-technical-comparator `
  --mi2-data-root data/private/mi2 `
  --mi4-data-root data/private/mi4 `
  --report-root reports/mi4
```

Outputs:

- `data/private/mi4/tree_walk_forward_predictions.parquet`
- `data/private/mi4/tree_forecast_scoreboard.parquet`
- `reports/mi4/tree_technical_forecast_scoreboard.md`
- `reports/mi4/tree_technical_forecast_scoreboard.json`

If the fixed MI-4 promotion gate fails, do not add further technical model types, parameter sweeps, or technical feature variations. The next research modality is controlled text/event research.

## MI-5 FOMC event/text foundation

MI-5 is a narrow descriptive event/text research slice. It builds a local corpus of official Federal Reserve FOMC statement HTML documents, resolves actual statement publication dates, applies conservative next-session availability, computes deterministic non-LLM lexical descriptors, and studies retrospective adjusted-close event windows across the MI-1 ETF universe.

```powershell
python -m market_intelligence_lab.cli run-mi5-fomc-event-text-foundation `
  --mi1-data-root data/private/mi1 `
  --mi5-data-root data/private/mi5 `
  --report-root reports/mi5
```

Outputs:

- `data/private/mi5/raw/`
- `data/private/mi5/manifests/fomc_raw_snapshot_manifest.parquet`
- `data/private/mi5/normalized/fomc_statement_event.parquet`
- `data/private/mi5/fomc_lexical_descriptor.parquet`
- `data/private/mi5/fomc_event_window_return.parquet`
- `reports/mi5/fomc_event_text_foundation.md`
- `reports/mi5/fomc_event_text_foundation.json`

MI-5 does not train a forecast model, form a portfolio, create a candidate signal, make a promotion claim, or use an LLM.

## MI-6 BLS release source qualification

MI-6 is a source-qualification-only phase for official BLS CPI and Employment Situation
release HTML. It qualifies whether official release documents provide enough verified embargo
timestamp evidence for a later forecast-research phase. It does not train a model, calculate
returns, form a portfolio, create a candidate signal, make a trading claim, or use an LLM.

```powershell
python -m market_intelligence_lab.cli run-mi6-bls-release-qualification `
  --mi6-data-root data/private/mi6 `
  --report-root reports/mi6
```

Outputs:

- `data/private/mi6/raw/`
- `data/private/mi6/manifests/bls_raw_snapshot_manifest.parquet`
- `data/private/mi6/normalized/bls_release_event.parquet`
- `reports/mi6/bls_release_source_qualification.md`
- `reports/mi6/bls_release_source_qualification.json`

MI-6 treats the actual fetched release HTML document as timestamp authority. A BLS event is
usable only when the release document itself contains an explicit date, time, and Eastern-time
designation, and usable rows are labelled `provider_timestamp_verified`.

## MI-7 SEC EDGAR 8-K acceptance source qualification

MI-7 is an `issuer_event_sidecar` source-qualification track for official SEC EDGAR Form 8-K
acceptance-time metadata. It is separate from the current 22-ETF promotion chain and does not
create an ETF forecast model, portfolio, candidate packet, broker integration, or GMA
integration.

```powershell
python -m market_intelligence_lab.cli run-mi7-sec-edgar-8k-acceptance-qualification `
  --mi7-data-root data/private/mi7 `
  --report-root reports/mi7
```

Outputs:

- `data/private/mi7/raw/`
- `data/private/mi7/manifests/sec_edgar_raw_snapshot_manifest.parquet`
- `data/private/mi7/normalized/sec_edgar_8k_acceptance_event.parquet`
- `reports/mi7/sec_edgar_8k_acceptance_qualification.md`
- `reports/mi7/sec_edgar_8k_acceptance_qualification.json`

MI-7 stores metadata only from the official SEC submissions API. It does not retrieve or parse
filing text. Any later 8-K event experiment requires either an individual-equity research track
with its own point-in-time stock-price panel or a separately approved time-aware
issuer-to-ETF exposure mapping based on documented historical holdings data.

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

## Historical holdout language

MI-2 through MI-4 historical holdout results are an observed development holdout.
They are not final programme-level promotion evidence.

Historical MI-8 replay records are operational and development evidence only.

Only prospective MI-8 records generated after the frozen protocol is established
may be considered in a future promotion decision.

No candidate packet, model, or strategy can be promoted from repeatedly viewed historical experimentation alone.
