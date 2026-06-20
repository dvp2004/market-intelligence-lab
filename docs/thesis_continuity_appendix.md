# Thesis-Continuity Appendix: NFLX Dissertation Baseline

## Evidence status

This appendix is provisional. The undergraduate thesis PDF has not been supplied to this repository bootstrap. The summary below is based on the public `nflx-hybrid-forecasting-trading-overlay` repository and must be checked against the PDF once provided.

## Original research question

Whether technical, fundamental, and sentiment feature combinations could improve next-day NFLX forecasting when tested with chronological, leakage-aware evaluation and strong persistence baselines.

## Datasets and time period

The repository reports a daily NFLX dataset with 1,137 trading-day rows covering 2018-01-02 through 2022-07-08. It combines OHLCV fields with sentiment aggregates and uses feature branches composed of technical, fundamental, and sentiment variables.

## Evaluation setup

- chronological train/test splitting;
- time-series cross-validation on the training segment;
- purged validation logic for rolling-window experiments;
- training-only scaling for LSTM models;
- persistence and zero-return baselines;
- Random Forest, XGBoost, and LSTM model families;
- a stylised, long-only, cost-aware rebalancing overlay.

## Main findings

- No final regression branch beat the persistence baseline for next-day NFLX price forecasting.
- The strongest directional effects were weak and did not establish a stable forecasting edge.
- Conservative overlay choices reduced losses relative to buy-and-hold in a poor NFLX window, but no final strategy produced a positive absolute return.
- Execution and risk-overlay design mattered at least as much as model selection.

## Limitations

- single surviving asset rather than a broad universe;
- short-horizon next-day focus;
- mixed source history without immutable source-snapshot and availability-evidence contracts;
- notebook and CSV centric workflow;
- stylised execution;
- branch-specific windows and fragile signal evidence;
- no proof of commercial or investable readiness.

## Continuing relevance

The new project retains the methodological discipline: chronological evaluation, baseline-first testing, redundancy checks, cautious treatment of negative results, and cost-aware evaluation. It rejects the NFLX-only scope, unversioned data assumptions, and using model output as direct trading authority.