# Logo Rotation PR Bot

This bot opens pull requests to rotate the homepage logo by date.

## How it works

- Workflow: `.github/workflows/logo-rotation-pr.yml`
- Script: `.github/logo-bot/update_logo.py`
- Config: `.github/logo-bot/events.json`

The workflow runs daily and:

1. Computes the active event window (fixed-date or lunar holiday window).
2. Updates the `logo:` field in `_config.yml`.
3. Opens or updates a PR only when the logo value changes.

## Event configuration

Edit `.github/logo-bot/events.json` to change windows or add new events.

Each event has:

- `name`: event identifier used in branch/PR naming.
- `logo`: path to logo image.
- `source_url`: event information URL (Wikipedia preferred). When set, homepage logo becomes clickable during that event window.
- `priority`: higher value wins if windows overlap.
- `rules`: one or more date rules.

Supported rule types:

- `fixed_range`
  - `start`: `MM-DD`
  - `end`: `MM-DD`
  - Supports year wrap (for example `12-15` to `01-05`).
- `holiday_window`
  - `country`: ISO country code used by `python-holidays`.
  - `contains`: substring used to match holiday names.
  - `start_offset`: days before holiday date.
  - `end_offset`: days after holiday date.

## Testing

Run workflow manually (`workflow_dispatch`) and set `date` to test any day.

You can also run locally:

```bash
python -m pip install -r .github/logo-bot/requirements.txt
python .github/logo-bot/update_logo.py --today 2026-12-20
```

## Notes on lunar events

Lunar event dates are resolved through `python-holidays` at runtime, which currently gives the expected dates for Chinese New Year, Diwali, and Eid al-Fitr for 2026-2030.
