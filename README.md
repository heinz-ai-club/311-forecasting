# 311 Service Forecasting

Forecasting Pittsburgh's 311 service requests (potholes, trash, streetlights and more) and measuring how long the City takes to resolve them, neighborhood by neighborhood, using the City's public data.

A Heinz AI Club (HAIC) project, November 2026 to April 2027.

## What we deliver

- **One cleaned dataset** of 311 requests
- **Sub-team A:** forecasts of request volume by type and neighborhood
- **Sub-team B:** resolution times and whether they differ by neighborhood, focusing on road and pothole requests
- **One shared dashboard** and an **equity memo** with findings the City or Council could act on

## Data source

[Pittsburgh 311 Data](https://data.wprdc.org/dataset/pittsburgh-311-data) from the Western Pennsylvania Regional Data Center, published by the City of Pittsburgh. One dataset covers 2015 to today and updates four times a day. Details in [`docs/DATA.md`](docs/DATA.md).

## How the two sub-teams work together

Both sub-teams write their results to files with agreed columns, and the dashboard reads those files. Nobody edits the same thing at once. The formats are in [`docs/FILE_FORMATS.md`](docs/FILE_FORMATS.md); change them only with agreement from both sub-teams and the dashboard owners.

## How the repo is organized

```
311-forecasting/
  src/            reusable code: download, clean, features
  notebooks/      exploration and modeling notebooks (prefix with your name)
  outputs/        small result files the dashboard reads (committed)
  dashboard/      the dashboard
  data/raw/       downloaded data (NOT committed; too large)
  data/processed/ cleaned data (NOT committed; recreate with src/)
  docs/           data guide and file formats
  haic.py         the helper for calling AI models
```

Raw and cleaned data are never committed to git: the full dataset is too large for GitHub. Anyone can recreate them with the scripts in `src/`.

## Get started

```bash
git clone https://github.com/heinz-ai-club/311-forecasting.git
cd 311-forecasting
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # only needed for AI tagging; key from your lead
python src/download.py           # downloads the data into data/raw/
```

Then read [`docs/DATA.md`](docs/DATA.md) before cleaning anything.

## AI use

Forecasting runs on your laptop or a free notebook; it needs no AI model. AI is used only to tag request descriptions into categories, with GPT-6 Luna:

```python
from haic import ask
label = ask(f"Classify this 311 request into one of: {categories}. Text: {text}", model="luna")
```

Test on 50 rows before running thousands. Our project's AI budget is small.

## Dashboard

Use a free tool: Power BI (free version), Tableau Public, or Streamlit. It reads only the files in `outputs/`.

## Rules

Read [`CONTRIBUTING.md`](CONTRIBUTING.md): pull requests only, keys only in `.env`.
