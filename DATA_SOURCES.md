## Data Source Notes

### Primary Source
- Name: DOTr eFOI Request - MRT-3 Daily Ridership 
- URL: https://www.foi.gov.ph/
- Format: CSV / XLSX / PDF
- Coverage: Daily ridership statistics, hourly entry/exit counts, and system-wide passenger volumes covering all MRT-3 stations.
- Why it fits the problem: This dataset provides the official, ground-truth commuter volume directly from the Department of Transportation. It directly answers the problem statement by giving us the exact number of passengers using each station, which is the exact metric needed to mathematically calculate platform overcrowding and simulate hours saved.
- Known limitations: Because this relies on an active eFOI request rather than a live API, there is a waiting period of up to 15 working days to receive the data. The data may also require manual cleaning if provided in PDF format instead of CSV.

### Fallback Source
- Name: Sakay.ph Metro Manila GTFS Data
- URL: https://github.com/sakayph/gtfs
- Format: CSV (stops.txt, trips.txt, stop_times.txt)
- Coverage: General Transit Feed Specification (GTFS) schedules, routes, and precise geographic coordinates for Metro Manila public transportation, including the MRT-3 line.
- Why it could still work: If the FOI DOTr portal is slow to provide exact peak-hour scheduled intervals, this open-source GTFS feed provides the geographic coordinates and the baseline train schedules needed to build the foundation of your "Headway Simulator".
- Known limitations: Because it is a static open-source feed, some of the baseline scheduled intervals might require manual updating to perfectly match current MRT-3 operations.