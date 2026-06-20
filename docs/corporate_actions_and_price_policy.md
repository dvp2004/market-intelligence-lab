# Corporate-Action and Price-Adjustment Policy

## Purpose

Price history has two different jobs. Decision-time technical features need the prices that were observable at the decision time. Later performance and return calculations need a documented economic return convention. These are not interchangeable.

## Raw OHLCV for decision-time technical features

- Store vendor-supplied raw `open`, `high`, `low`, `close`, and `volume` separately from adjusted values.
- Technical features intended to represent observable close-to-close information use raw OHLCV unless a feature explicitly documents another basis.
- A vendor's retrospectively back-adjusted history is not described as verified point-in-time truth.
- Any historical use of a back-adjusted series must state its availability evidence level and adjustment basis.

## Adjusted prices and later evaluation

- Keep vendor-adjusted close or a separately computed total-return index in distinct fields.
- Use an explicitly documented total-return convention for later target construction, benchmark comparison, and portfolio evaluation.
- Do not substitute adjusted history into raw decision-time features without a separately approved policy and audit.

## Splits

- Record splits as corporate-action events with effective date, source, retrieval timestamp, and availability evidence level.
- Preserve raw historical bars as supplied in their source snapshot.
- Maintain any split-adjusted analytical series separately and label its calculation or vendor basis.

## Dividends

- Treat raw close as a price series, not a total-return series.
- Use a documented dividend-aware adjusted or total-return series only for later return calculations where appropriate.
- Do not assume a dividend adjustment was known at a historical decision timestamp without evidence.

## Ticker changes and delistings

- Keep a stable `instrument_id`; symbols are attributes with effective-date ranges.
- Preserve former tickers and lifecycle events in the instrument registry.
- Delisted instruments remain in historical coverage and cannot be silently removed from a universe because they disappeared later.

## Vendor back-adjustments

- Record adjustment basis, retrieval timestamp, snapshot identifier, and evidence level.
- Vendor back-adjusted data may be useful for retrospective evaluation, but it is never automatically treated as the historical value available at a past decision time.
- Any future claim of point-in-time validity requires source-specific evidence or an approved contractual assumption.