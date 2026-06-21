# Implementation Roadmap

## Status Tracker

- MI-0: complete.
- MI-1: complete.
- MI-2: complete.
- MI-3: complete.
- MI-4: complete; final technical-model-family comparator.
- MI-5: complete; FOMC event/text foundation.
- MI-6: complete; final source-qualification-only phase for official BLS CPI and
  Employment Situation release timestamp evidence.
- MI-7: active; `issuer_event_sidecar` source-qualification track for SEC EDGAR
  Form 8-K acceptance-time metadata.
- MI-8+: not started by default; do not add another standalone source-qualification
  prompt after the one real MI-7 run unless explicitly approved.

MI-4 is the final technical-model-family comparator. If its fixed promotion gate fails, do not add further technical model types, parameter sweeps, or technical feature variations. The next research modality is controlled text/event research.

MI-5 is descriptive event/text research only. It does not create a forecast model, portfolio, candidate signal, promotion claim, or LLM phase.

MI-6 is source qualification only. If it qualifies, a later BLS release-event forecast test must
be pre-registered, frozen before a prospective shadow period, and limited to clearly specified
next-session or multi-session outcomes. Daily EOD ETF data cannot measure the immediate
8:30 a.m. reaction precisely and must not be used to claim intraday event-capture ability.

MI-7 is an `issuer_event_sidecar` source-qualification track, not part of the current 22-ETF
promotion chain. A successful MI-7 qualification must not automatically lead to an ETF forecast
model. Before any later 8-K event experiment, choose either an individual-equity research track
with its own point-in-time stock-price panel or a separately approved time-aware issuer-to-ETF
exposure mapping based on documented historical holdings data. Without one of those routes,
MI-7 ends as a reusable data capability only.

MI-2 through MI-4 historical holdout results are an observed development holdout.
They are not final programme-level promotion evidence.

Historical MI-8 replay records are operational and development evidence only.

Only prospective MI-8 records generated after the frozen protocol is established
may be considered in a future promotion decision.

No candidate packet, model, or strategy can be promoted from repeatedly viewed historical experimentation alone.

GMA remains the actual paper-trading and portfolio-construction track. Market Intelligence Lab
remains research-only until a source family proves incremental forecast value under a frozen
prospective protocol.
