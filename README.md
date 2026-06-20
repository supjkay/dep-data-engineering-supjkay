# Predictive Rail Impact: Modeling Commuter Wait Times

## Problem Statement
**Question:** If the MRT-3 and LRT-1 reduce their peak-hour train frequency (headway) by exactly 2 minutes through the deployment of additional train sets, how many cumulative passenger waiting hours would be saved weekly, and which specific stations would experience the most significant drop in platform crowding?

## Target Audience
The **Department of Transportation (DOTr)**, **Light Rail Transit Authority (LRTA)**, and **Metro Rail Transit Corporation (MRTC)**. They need data-backed models to justify the massive capital expenditure required to purchase and deploy new train cars.

## Key Performance Indicators (KPIs)
1. **Weekly Passenger Waiting Hours Saved:** The aggregate time saved across all commuters at the platform level due to faster train arrivals.
2. **Platform Crowding Index:** A calculated metric based on passenger boarding volume per minute compared to the station's physical holding capacity.

## Data Sources
* **FOI DOTr Open Data Portal:** [www.foi.gov.ph](https://www.foi.gov.ph/) (For historical MRT-3/LRT ridership volumes, hourly entry/exit counts, and station dimensions).
* **Metro Manila GTFS Data:** [github.com/sakayph/gtfs](https://github.com/sakayph/gtfs) (For transit schedules and route geometries to establish baseline headways).

## Final Dashboard Concept
An interactive "Headway Impact Simulator" for rail planners. The main view features a schematic map of the MRT/LRT lines. A slider allows users to adjust the "Target Peak-Hour Headway" (e.g., from 5 minutes down to 3 minutes). As the slider moves, a primary KPI counter updates to show the total weekly hours saved for commuters. Individual stations on the map change color from red (overcrowded) to green (optimal) based on the simulated passenger throughput.