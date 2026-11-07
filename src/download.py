"""
Download the full Pittsburgh 311 CSV into data/raw/311_data.csv.

Usage:
    python src/download.py            # skips if the file already exists
    python src/download.py --force    # download again

The file is large and is never committed to git (data/raw/ is ignored).
Source and notes: docs/DATA.md
"""

import argparse
import sys
from pathlib import Path

import requests

# The full download link from docs/DATA.md.
DUMP_URL = "https://data.wprdc.org/datastore/dump/5202679a-d243-402e-b82a-63189995a942"
OUT_PATH = Path(__file__).resolve().parent.parent / "data" / "raw" / "311_data.csv"
CHUNK = 1024 * 1024  # read 1 MB at a time so memory use stays small


def download(force: bool = False) -> int:
    if OUT_PATH.exists() and not force:
        print(f"{OUT_PATH} already exists. Use --force to download it again.")
        return 0

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = OUT_PATH.with_suffix(".csv.part")  # so a failed download never leaves a half file

    try:
        with requests.get(DUMP_URL, stream=True, timeout=60) as resp:
            resp.raise_for_status()
            # The server may not send a size (the file is generated on the fly).
            total = int(resp.headers.get("Content-Length", 0))
            done = 0
            with open(tmp_path, "wb") as f:
                for chunk in resp.iter_content(CHUNK):
                    f.write(chunk)
                    done += len(chunk)
                    if total:
                        print(f"\rDownloaded {done / 1e6:.0f} of {total / 1e6:.0f} MB", end="", flush=True)
                    else:
                        print(f"\rDownloaded {done / 1e6:.0f} MB", end="", flush=True)
        print()
    except requests.exceptions.RequestException as exc:
        tmp_path.unlink(missing_ok=True)
        print(f"\nDownload failed: {exc}\nCheck your internet connection and try again.", file=sys.stderr)
        return 1
    except OSError as exc:
        tmp_path.unlink(missing_ok=True)
        print(f"\nCould not write the file: {exc}\nCheck that you have enough disk space.", file=sys.stderr)
        return 1

    tmp_path.replace(OUT_PATH)
    print(f"Saved {OUT_PATH}")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download the Pittsburgh 311 data.")
    parser.add_argument("--force", action="store_true", help="download even if the file exists")
    sys.exit(download(parser.parse_args().force))
