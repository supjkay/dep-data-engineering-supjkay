# Beating the Rush: The Metro Manila Rail Dashboard

## Problem Statement
**I want to answer:** If we cut peak-hour waiting times on the MRT-3 by exactly 2 minutes, how many total hours will commuters save every week, and which specific stations will see the biggest drop in platform overcrowding?

## Target Audience
This project is for the **Department of Transportation (DOTr)**, **Metro Manila transit planners**, and **everyday commuters** who want to anticipate and avoid station overcrowding.

## Key Performance Indicators (KPIs)
To serve both audiences, the main metrics I want to track are:
1. Total Commuter Hours Saved (System-wide impact)
2. Peak Platform Crowding Density (Safety and congestion)
3. Average Platform Wait Time (Individual commuter experience)
4. Optimal Travel Windows (Best/worst times to ride)

## Data Sources
* **FOI DOTr Open Data Portal:** [www.foi.gov.ph](https://www.foi.gov.ph/) (For historical MRT-3 ridership volumes, hourly entry/exit counts, and station dimensions).
* **Metro Manila GTFS Data:** [github.com/sakayph/gtfs](https://github.com/sakayph/gtfs) (For transit schedules and route geometries to establish baseline headways).

## Final Dashboard Concept
An interactive "Headway Impact Simulator" for rail planners. The main view features a schematic map of the MRT lines. A slider allows users to adjust the "Target Peak-Hour Headway" (e.g., from 5 minutes down to 3 minutes). As the slider moves, a primary KPI counter updates to show the total weekly hours saved for commuters. Individual stations on the map change color from red (overcrowded) to green (optimal) based on the simulated passenger throughput.


## Data Sources & Ingestion Method

### Primary Source
- **Name:** DOTr eFOI Request — MRT-3 Daily Ridership
- **URL:** https://www.foi.gov.ph/
- **Format:** XLSX (Excel Spreadsheet)
- **Access Path & Ingestion Strategy:** Downloaded directly from the government eFOI portal. Local ingestion is handled programmatically via `scripts/ingest.py`, which uses Python's `shutil` library to safely copy the raw file, standardize its filename to `mrt3_hourly_ridership_2026_raw.xlsx`, and lock it into the `/data/raw/` directory.
- **Coverage:** Hourly passenger entry/exit counts across all 13 MRT-3 stations covering January to June 2026.
- **Why it fits the problem:** This provides the ground-truth commuter volume needed to establish the baseline for our Headway Simulator and mathematically model platform overcrowding.

### Backup / Fallback Source
- **Name:** Sakay.ph Metro Manila GTFS Data
- **URL:** https://github.com/sakayph/gtfs
- **Format:** CSV (`stops.txt`, `trips.txt`, `stop_times.txt`)
- **Access Path & Ingestion Strategy:** Programmatic download via Python's `urllib.request` directly from the open-source GitHub repository into `/data/raw/`.

---

## Simulation Assumptions (Platform Crowding)
Since the raw DOTr ridership data provides hourly entry/exit aggregations rather than minute-by-minute turnstile logs, our Headway Simulator infers platform crowding using the following baseline mathematical assumptions:
1. **Uniform Passenger Arrival Rate:** We assume commuters enter the station at a relatively uniform rate across a given hour (e.g., an hourly volume of 600 passengers equates to an arrival rate of 10 passengers per minute).
2. **Crowding Accumulation:** Platform crowding is calculated as the accumulated difference between the minute-by-minute passenger arrival rate and the clearance capacity of the trains arriving at the scheduled headway.
3. **Fixed Train Capacity:** Train carrying capacity is assumed constant per trip for the sake of baseline headway impact calculations.