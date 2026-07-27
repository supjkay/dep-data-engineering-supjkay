# Data Source Notes

## Primary Source
- **Name:** DOTr eFOI Request — MRT-3 Daily Ridership
- **URL:** https://www.foi.gov.ph/
- **Format:** XLSX (Excel Spreadsheet)
- **Access Path & Ingestion Strategy:** Downloaded directly from the government eFOI portal. Local ingestion is handled programmatically via `scripts/ingest.py`, which uses Python's `shutil` library to safely copy the raw file (`Leandra Oania.xlsx`), standardize its filename to `mrt3_hourly_ridership_2026_raw.xlsx`, and lock it into the `/data/raw/` directory.
- **Coverage:** Hourly passenger entry/exit counts across all 13 MRT-3 stations covering January to June 2026.
- **Why it fits the problem:** This provides the ground-truth commuter volume needed to establish the baseline for our Headway Simulator and mathematically model platform overcrowding.
- **Known limitations:** Manual acquisition via eFOI request is required rather than an automated live API feed.

## Backup / Fallback Source
- **Name:** Sakay.ph Metro Manila GTFS Data
- **URL:** https://github.com/sakayph/gtfs
- **Format:** CSV (`stops.txt`, `trips.txt`, `stop_times.txt`)
- **Access Path & Ingestion Strategy:** Programmatic download via Python's `urllib.request` directly from the open-source GitHub repository into `/data/raw/`.
- **Coverage:** General Transit Feed Specification (GTFS) schedules, routes, and geographic coordinates for Metro Manila public transit, specifically including the MRT-3 line.
- **Why it fits the problem:** If exact operational interval logs are unavailable, this feed provides the baseline train schedules and geographic station spacing required to build the foundational headway simulation logic.

## Problem Statement Clarification
*Note on Headway vs. Waiting Time:* In our problem statement, the targeted **"2-minute reduction"** refers specifically to **train headway** (the operational, scheduled time interval between consecutive train arrivals). Reducing the train headway is the operational lever that cascades into our primary KPI: reducing actual passenger waiting time and platform congestion during peak hours.