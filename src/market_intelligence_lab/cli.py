"""Command-line entry points for Market Intelligence Lab."""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import date
from pathlib import Path

from market_intelligence_lab.data.adapter_yfinance import YFinanceEodAdapter
from market_intelligence_lab.data.pipeline import load_source_config, refresh_mi1_market_data
from market_intelligence_lab.quality.validation import DataQualityError


def _parse_date(value: str) -> date:
    return date.fromisoformat(value)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="market_intelligence_lab")
    subparsers = parser.add_subparsers(dest="command")

    refresh = subparsers.add_parser(
        "refresh-mi1-market-data",
        help="Refresh research-only MI-1 daily ETF EOD market data.",
    )
    refresh.add_argument("--universe-config", type=Path, required=True)
    refresh.add_argument("--source-config", type=Path, required=True)
    refresh.add_argument("--data-root", type=Path, required=True)
    refresh.add_argument("--report-root", type=Path, required=True)
    refresh.add_argument("--start", type=_parse_date, required=True)
    refresh.add_argument(
        "--end",
        type=_parse_date,
        default=None,
        help="Optional inclusive end date. Omit to let the source adapter request latest data.",
    )
    refresh.add_argument(
        "--mi2-registry-config",
        type=Path,
        default=Path("configs/mi2_research_registry.yaml"),
    )
    return parser


def format_data_quality_error(error: DataQualityError, raw_root: Path) -> str:
    event_counts = Counter(event.event_type for event in error.events)
    lines = [
        "MI-1 refresh failed closed during data-quality validation.",
        "validation_event_counts:",
    ]
    for event_type, count in sorted(event_counts.items()):
        lines.append(f"  {event_type}: {count}")
    lines.append("validation_examples:")
    for event in error.events[:10]:
        session = "" if event.session_date is None else event.session_date.isoformat()
        instrument = event.instrument_id or ""
        lines.append(
            f"  {event.severity} {event.event_type} "
            f"instrument_id={instrument} session_date={session} message={event.message}"
        )
    lines.append(f"local_raw_snapshot_path: {raw_root}")
    lines.append("Raw provider payloads are local-only and are not printed by this command.")
    return "\n".join(lines)


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()
    if args.command != "refresh-mi1-market-data":
        print("Market Intelligence Lab: MI-0 complete; MI-1 market-data command available.")
        return

    source_config = load_source_config(args.source_config)
    if source_config.adapter != "yfinance":
        raise SystemExit(f"Unsupported MI-1 source adapter: {source_config.adapter}")
    adapter = YFinanceEodAdapter(
        auto_adjust=source_config.auto_adjust,
        actions=source_config.actions,
    )
    try:
        result = refresh_mi1_market_data(
            universe_config=args.universe_config,
            source_config_path=args.source_config,
            mi2_registry_config=args.mi2_registry_config,
            data_root=args.data_root,
            report_root=args.report_root,
            start=args.start,
            end=args.end,
            adapter=adapter,
        )
    except DataQualityError as error:
        raise SystemExit(format_data_quality_error(error, args.data_root / "raw")) from error

    print(f"run_id: {result.run_id}")
    print(f"source: {result.source_name}")
    print(f"availability_evidence_level: {result.evidence_level}")
    print(f"snapshot_count: {result.snapshot_count}")
    print(f"bar_count: {result.bar_count}")
    print(f"corporate_action_count: {result.corporate_action_count}")
    if result.common_research_start_date is None:
        print(
            "coverage_common_research_start_date: BLOCKED "
            f"({result.common_research_start_blocked_reason})"
        )
    else:
        print(f"coverage_common_research_start_date: {result.common_research_start_date}")
    print(
        "decision_panel_availability: "
        f"{'PASS' if result.decision_panel_availability_pass else 'FAIL'}"
    )
    print("output_paths:")
    for name, path in result.output_paths.items():
        print(f"  {name}: {path}")


if __name__ == "__main__":
    main()
