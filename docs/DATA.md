# Data guide

Checked November 7, 2026. Confirm on the WPRDC pages before relying on any detail.

## The dataset

**Pittsburgh 311 Data** on the Western Pennsylvania Regional Data Center (WPRDC):
https://data.wprdc.org/dataset/pittsburgh-311-data

- The City moved to a new 311 system on **February 4, 2025**.
- This dataset contains the new system's records **and all records back to the previous system's launch in 2015**, so one dataset covers the whole history.
- It is updated four times a day.
- Requests come from phone calls, social media, email, the City website, and the 311 app.
- For privacy, the exact location of some complaint types is not published.

Resources on that page:

| Resource | What it is |
| --- | --- |
| 311 Data (CSV) | The requests. Full download: https://data.wprdc.org/datastore/dump/5202679a-d243-402e-b82a-63189995a942 |
| 311 Data Dictionary (XLSX) | What each column means. **Read this first** |
| 311 Issue, Subject Code, and Public Access (XLSX) | The list of request types (issues) and their codes |
| 311 Data User Guide | Background on how the data is collected |

There is also an older archive, **311 Data Archive** (https://data.wprdc.org/dataset/311-data), which stopped updating on February 4, 2025. You should not need it, except to look up old request type names.

## Things to watch for

1. **Request types changed with the new system.** Old and new records may name the same issue differently. Before forecasting across 2025, build a mapping table from old types to new issue categories (use both codebooks), and save it as `data/reference/category_map.csv`.
2. **The 2025 switch can look like a real change.** A jump or drop in volume around February 2025 may be the system change, not the city. Check before modeling it as a trend.
3. **Column names:** use the Data Dictionary for the exact names and record them in `src/columns.py`, so the code uses one set of names everywhere.
4. **Missing locations:** some types have no exact location. Neighborhood-level analysis is safer than street-level.
5. **Resolution time** needs both a created and a closed timestamp. Open requests have no closed time; do not treat them as zero.
6. **The file is large.** Download once into `data/raw/` and keep it out of git.
7. **Council district comes as text like `D9` in the raw data;** `clean.py` converts it to an integer to match `FILE_FORMATS.md`.

## Who does what

- **Sub-team A** owns `src/download.py` and `src/clean.py`, which produce `data/processed/clean_311.csv` in the format in `FILE_FORMATS.md`.
- **Sub-team B** starts on the category map and the neighborhood boundaries while cleaning is in progress.
