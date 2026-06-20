# MI-0 Continuation Map

## Retain

### From the NFLX dissertation repository

- chronological training and evaluation;
- purged validation logic where labels overlap;
- training-only transformations;
- persistence and zero-return baselines;
- feature-provenance and redundancy audits;
- prediction exports and cost-aware evaluation;
- honest reporting when complex models fail to establish a dependable edge.

### From Market Strats Lab

- point-in-time and post-endpoint separation;
- immutable accepted inputs and reproducible checkpoints;
- data-quality, cost, drawdown, turnover, and robustness controls;
- fail-closed operational safeguards;
- strict separation of research signals from portfolio construction and paper execution.

## Keep isolated

This repository must not duplicate GMA portfolio construction, risk limits, strategy tournament, paper-readiness, manual TradingView paper workflow, fill validation, reconciliation, broker adapters, credentials, or order submission.

## Do not repeat

- single-asset NFLX-only scope;
- next-day price-level forecasting as the sole objective;
- notebook-first or CSV-sprawl architecture;
- unversioned source history;
- treating vendor back-adjusted prices as verified historical decision-time truth;
- equating lower loss versus buy-and-hold with an investable edge;
- repeated tuning on an untouched holdout;
- feature-family expansion without incremental-value evidence.

## What belongs here

- immutable market-data snapshot manifests;
- point-in-time data contracts and availability evidence;
- market-data quality, coverage, and availability audits;
- later feature-family experiments and research reports;
- broker-neutral research-only candidate signal packets.

## Future candidate export boundary

A future candidate packet may contain `decision_timestamp`, `asset`, `horizon`, `expected_return`, `expected_excess_return`, `probability_positive_return`, `predicted_volatility`, `confidence`, `uncertainty`, `abstain`, `signal_direction`, `model_version`, `feature_snapshot_id`, and `data_snapshot_ids`.

It must also contain `research_only = true` and `portfolio_influence = 0`. It must never contain direct orders, target weights, broker instructions, credentials, or authority to alter GMA.