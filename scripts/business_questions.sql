-- ==============================================================================
-- MRT-3 Headway Simulation: Baseline Business Questions
-- Dataset: processed_mrt3_ridership (Long format)
-- ==============================================================================

-- ------------------------------------------------------------------------------
-- Question 1: Which hour of the day experiences the highest average passenger 
-- arrival rate across the entire MRT-3 line?
-- Context: Identifying absolute peak hours is critical for the simulation, 
-- as this is when the 2-minute headway reduction will have the biggest impact.
-- ------------------------------------------------------------------------------
SELECT 
    hour_start, 
    AVG(arrival_rate_per_min) AS avg_system_arrival_rate_per_min
FROM 
    processed_mrt3_ridership
GROUP BY 
    hour_start
ORDER BY 
    avg_system_arrival_rate_per_min DESC;


-- ------------------------------------------------------------------------------
-- Question 2: Which 5 stations handle the highest total volume of entering 
-- passengers, making them the most vulnerable to platform overcrowding?
-- Context: These stations will serve as the primary stress-test locations 
-- for the headway simulation.
-- ------------------------------------------------------------------------------
SELECT 
    station_name, 
    SUM(hourly_entries) AS total_passenger_entries
FROM 
    processed_mrt3_ridership
GROUP BY 
    station_name
ORDER BY 
    total_passenger_entries DESC
LIMIT 5;


-- ------------------------------------------------------------------------------
-- Question 3: What is the absolute maximum passenger arrival rate recorded 
-- at each station in a single hour?
-- Context: While average rates are useful, simulating against the absolute 
-- maximum historical load ensures the headway reduction is tested against 
-- worst-case scenarios.
-- ------------------------------------------------------------------------------
SELECT 
    station_name, 
    MAX(arrival_rate_per_min) AS max_peak_arrival_rate_per_min
FROM 
    processed_mrt3_ridership
GROUP BY 
    station_name
ORDER BY 
    max_peak_arrival_rate_per_min DESC;