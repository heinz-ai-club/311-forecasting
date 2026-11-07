# Shared file formats

The two sub-teams and the dashboard connect through these files. Keep the column names and types exactly as listed. To change a format, agree with both sub-teams and the dashboard owners, then update this page in the same pull request.

## data/processed/clean_311.csv (not committed; made by `src/clean.py`)

Made by: Sub-team A. Used by: everyone.

| Column | Type | Notes |
| --- | --- | --- |
| `request_id` | string | Unique id from the source data |
| `created_at` | datetime (ISO 8601) | When the request was made |
| `closed_at` | datetime or empty | Empty if still open |
| `status` | string | As in the source, e.g. open or closed |
| `category` | string | Harmonized category from `data/reference/category_map.csv` |
| `source_type` | string | Original request type from the source |
| `neighborhood` | string | City neighborhood name |
| `council_district` | integer or empty | If available |
| `origin` | string | Phone, website, app, and so on, if available |

## outputs/forecasts.csv (committed)

Made by: Sub-team A. Used by: dashboard.

| Column | Type | Notes |
| --- | --- | --- |
| `date` | date (YYYY-MM-DD) | Start of the forecast period |
| `period` | string | `week` or `month` |
| `category` | string | Harmonized category |
| `neighborhood` | string | Or `ALL` for citywide |
| `forecast` | number | Expected number of requests |
| `low` | number | Lower bound of the prediction interval |
| `high` | number | Upper bound of the prediction interval |
| `model` | string | Model name, e.g. `prophet_v2` |

## outputs/resolution_times.csv (committed)

Made by: Sub-team B. Used by: dashboard and memo.

| Column | Type | Notes |
| --- | --- | --- |
| `category` | string | Harmonized category |
| `neighborhood` | string | City neighborhood name |
| `n_closed` | integer | Closed requests counted |
| `median_days_to_close` | number | Median days from created to closed |
| `p90_days_to_close` | number | 90th percentile |
| `pct_open_over_30_days` | number | Share of requests still open after 30 days, 0 to 1 |
| `equity_index` | number | Defined in `docs/EQUITY_INDEX.md` by Sub-team B |
| `period_start` | date | Start of the time window measured |
| `period_end` | date | End of the time window measured |

## Sample rows

Until the real files exist, the dashboard owners can build against sample files in `outputs/samples/` with a few made-up rows in exactly these formats. Delete the samples once real outputs exist.
