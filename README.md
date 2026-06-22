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