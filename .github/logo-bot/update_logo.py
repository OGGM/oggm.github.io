#!/usr/bin/env python3
"""Compute the active celebration logo and update _config.yml accordingly."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
from typing import Dict, Iterable, List, Optional, Tuple

import holidays


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--events-file",
        default=".github/logo-bot/events.json",
        help="Path to event configuration JSON.",
    )
    parser.add_argument(
        "--today",
        default="",
        help="Override date in YYYY-MM-DD format for testing.",
    )
    parser.add_argument(
        "--github-output",
        default="",
        help="Path to the GitHub Actions output file.",
    )
    return parser.parse_args()


def parse_mmdd(mmdd: str) -> Tuple[int, int]:
    month_str, day_str = mmdd.split("-")
    return int(month_str), int(day_str)


def fixed_windows(rule: Dict, today: dt.date) -> Iterable[Tuple[dt.date, dt.date]]:
    start_mm, start_dd = parse_mmdd(rule["start"])
    end_mm, end_dd = parse_mmdd(rule["end"])
    wraps = (end_mm, end_dd) < (start_mm, start_dd)

    for year in (today.year - 1, today.year, today.year + 1):
        start = dt.date(year, start_mm, start_dd)
        end_year = year + 1 if wraps else year
        end = dt.date(end_year, end_mm, end_dd)
        yield start, end


def holiday_anchor_dates(rule: Dict, today: dt.date) -> List[dt.date]:
    years = [today.year - 1, today.year, today.year + 1]
    country = rule["country"]
    token = rule["contains"].lower()

    holiday_map = holidays.country_holidays(country, years=years, language="en")
    grouped: Dict[int, List[dt.date]] = {}

    for holiday_date, holiday_name in holiday_map.items():
        if token in holiday_name.lower():
            grouped.setdefault(holiday_date.year, []).append(holiday_date)

    return [min(v) for _, v in sorted(grouped.items())]


def holiday_windows(rule: Dict, today: dt.date) -> Iterable[Tuple[dt.date, dt.date]]:
    start_offset = int(rule.get("start_offset", 0))
    end_offset = int(rule.get("end_offset", 0))
    for anchor in holiday_anchor_dates(rule, today):
        yield anchor + dt.timedelta(days=start_offset), anchor + dt.timedelta(days=end_offset)


def active_window_for_rule(rule: Dict, today: dt.date) -> Optional[Tuple[dt.date, dt.date]]:
    rule_type = rule["type"]
    if rule_type == "fixed_range":
        windows = fixed_windows(rule, today)
    elif rule_type == "holiday_window":
        windows = holiday_windows(rule, today)
    else:
        raise ValueError(f"Unsupported rule type: {rule_type}")

    for start, end in windows:
        if start <= today <= end:
            return start, end
    return None


def active_event(events: List[Dict], today: dt.date) -> Tuple[Optional[Dict], Optional[Tuple[dt.date, dt.date]]]:
    candidates: List[Tuple[int, str, Dict, Tuple[dt.date, dt.date]]] = []

    for event in events:
        for rule in event.get("rules", []):
            window = active_window_for_rule(rule, today)
            if window:
                priority = int(event.get("priority", 0))
                candidates.append((priority, event["name"], event, window))
                break

    if not candidates:
        return None, None

    candidates.sort(key=lambda item: (-item[0], item[1]))
    _, _, event, window = candidates[0]
    return event, window


def replace_logo(config_text: str, desired_logo: str) -> Tuple[str, bool, Optional[str]]:
    pattern = re.compile(r"^(logo:\s*)(\S+)(\s*)$", re.MULTILINE)
    match = pattern.search(config_text)
    if not match:
        raise RuntimeError("Could not find a top-level logo setting in _config.yml")

    current_logo = match.group(2)
    if current_logo == desired_logo:
        return config_text, False, current_logo

    new_text = pattern.sub(rf"\1{desired_logo}\3", config_text, count=1)
    return new_text, True, current_logo


def replace_logo_event_url(config_text: str, desired_url: str) -> Tuple[str, bool, str]:
    key = "logo_event_url"
    desired_value = f'"{desired_url}"' if desired_url else '""'
    pattern = re.compile(rf"^({key}:\s*)(.*?)(\s*)$", re.MULTILINE)
    match = pattern.search(config_text)

    if match:
        current_value = match.group(2).strip().strip('"')
        if current_value == desired_url:
            return config_text, False, current_value
        new_text = pattern.sub(rf"\1{desired_value}\3", config_text, count=1)
        return new_text, True, current_value

    logo_line = re.search(r"^logo:\s*\S+\s*$", config_text, re.MULTILINE)
    insertion = f"{key}: {desired_value}\n"

    if logo_line:
        insert_at = logo_line.end()
        new_text = config_text[:insert_at] + "\n" + insertion + config_text[insert_at:]
    else:
        suffix = "" if config_text.endswith("\n") else "\n"
        new_text = config_text + suffix + insertion

    return new_text, True, ""


def emit_outputs(path: str, outputs: Dict[str, str]) -> None:
    if not path:
        return
    out_path = pathlib.Path(path)
    with out_path.open("a", encoding="utf-8") as f:
        for key, value in outputs.items():
            f.write(f"{key}={value}\n")


def main() -> int:
    args = parse_args()
    repo_root = pathlib.Path.cwd()
    events_path = repo_root / args.events_file

    with events_path.open("r", encoding="utf-8") as f:
        cfg = json.load(f)

    if args.today:
        today = dt.date.fromisoformat(args.today)
    else:
        today = dt.date.today()

    event, window = active_event(cfg["events"], today)
    if event:
        desired_logo = event["logo"]
        desired_event_url = event.get("source_url", "")
        event_name = event["name"]
        window_str = f"{window[0].isoformat()}..{window[1].isoformat()}"
    else:
        desired_logo = cfg["default_logo"]
        desired_event_url = ""
        event_name = "default"
        window_str = "none"

    target_config = repo_root / cfg.get("target_config", "_config.yml")
    original = target_config.read_text(encoding="utf-8")
    updated_logo, logo_changed, current_logo = replace_logo(original, desired_logo)
    updated, url_changed, current_event_url = replace_logo_event_url(updated_logo, desired_event_url)
    changed = logo_changed or url_changed

    if changed:
        target_config.write_text(updated, encoding="utf-8")

    safe_name = re.sub(r"[^a-z0-9-]+", "-", event_name.lower()).strip("-") or "default"
    branch = f"bot/logo-{safe_name}-{today.isoformat()}"
    commit_message = f"chore: set logo to {event_name} ({today.isoformat()})"
    pr_title = f"chore: rotate logo for {event_name} ({today.isoformat()})"

    outputs = {
        "changed": "true" if changed else "false",
        "event_name": event_name,
        "desired_logo": desired_logo,
        "current_logo": current_logo or "",
        "window": window_str,
        "event_url": desired_event_url,
        "current_event_url": current_event_url,
        "branch": branch,
        "commit_message": commit_message,
        "pr_title": pr_title,
    }
    emit_outputs(args.github_output, outputs)

    print(f"today={today.isoformat()}")
    print(f"event={event_name}")
    print(f"window={window_str}")
    print(f"current_logo={current_logo}")
    print(f"desired_logo={desired_logo}")
    print(f"current_event_url={current_event_url}")
    print(f"desired_event_url={desired_event_url}")
    print(f"changed={outputs['changed']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
