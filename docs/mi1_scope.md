# MI-1 Scope: One Market-Data Vertical Slice

## Deliver

- fixed 22-ETF instrument registry;
- daily end-of-day market-data adapter selected under public-data policy;
- immutable raw snapshot manifest;
- normalized Parquet output;
- coverage audit;
- availability-time audit;
- one reproducible refresh command and visible reports.

## Do not deliver in MI-1

- macro registry, macro data, or macro features;
- fundamentals, news, sentiment, or LLM processing;
- technical features or models;
- portfolio construction or simulation;
- broker integration, orders, credentials, or real-money workflows.

Macro data begins no earlier than MI-3, after market-data contracts, coverage reporting, and availability audits are stable.