"""Check that the sample files have exactly the columns in docs/FILE_FORMATS.md."""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FORECASTS = ["date", "period", "category", "neighborhood", "forecast", "low", "high", "model"]
RESOLUTION = [
    "category", "neighborhood", "n_closed", "median_days_to_close", "p90_days_to_close",
    "pct_open_over_30_days", "equity_index", "period_start", "period_end",
]


def read(name):
    with open(ROOT / "outputs" / "samples" / name, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        return reader.fieldnames, rows


def test_forecasts_columns():
    columns, rows = read("forecasts.csv")
    assert columns == FORECASTS
    assert len(rows) == 5


def test_resolution_times_columns():
    columns, rows = read("resolution_times.csv")
    assert columns == RESOLUTION
    assert len(rows) == 5


def test_column_constants_match_real_file_header():
    # The header of the real dump, checked November 7, 2026.
    from src.columns import ALL_COLUMNS

    assert len(ALL_COLUMNS) == len(set(ALL_COLUMNS)) == 26
    assert ALL_COLUMNS[0] == "_id" and ALL_COLUMNS[-1] == "unique_id"
