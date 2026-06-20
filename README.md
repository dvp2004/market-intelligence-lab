# Market Intelligence Lab

A research-only, point-in-time market-intelligence platform for testing whether carefully defined information families improve risk-adjusted allocation research over transparent baselines.

`market-intelligence-lab` complements `market-strats-lab`. It does not replace or duplicate GMA portfolio construction, risk controls, tournament selection, paper-readiness, manual TradingView workflow, fill validation, reconciliation, broker adapters, or execution controls.

## Current status

**MI-0 foundation only.** The repository contains research boundaries, market-data contracts, the fixed 22-ETF universe, corporate-action policy, availability-evidence policy, public-data policy, and a pre-registered MI-2 research registry.

It does not contain:

- market-data ingestion;
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