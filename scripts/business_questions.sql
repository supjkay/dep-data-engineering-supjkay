-- ==============================================================================
-- MRT-3 Headway Simulation: Baseline Business Questions
-- Dataset: processed_mrt3_ridership (Long format)
-- ==============================================================================

-- ------------------------------------------------------------------------------
-- Question 1: Which hour of the day experiences the highest average passenger 
-- arrival rate across the entire MRT-3 line?
-- ------------------------------------------------------------------------------
SELECT 
    time_interval, 
    ROUND(AVG(arrival_rate_per_min)) AS avg_system_arrival_rate_per_min
FROM 
    processed_mrt3_ridership
WHERE 
    action = 'entry'
GROUP BY 
    time_interval
ORDER BY 
    avg_system_arrival_rate_per_min DESC;

-- ------------------------------------------------------------------------------
-- Question 2: Which 5 stations handle the highest total volume of entering 
-- passengers, making them the most vulnerable to platform overcrowding?
-- ------------------------------------------------------------------------------
SELECT 
    station_name, 
    SUM(passenger_count) AS total_passenger_entries
FROM 
    processed_mrt3_ridership
WHERE 
    action = 'entry'
GROUP BY 
    station_name
ORDER BY 
    total_passenger_entries DESC
LIMIT 5;

-- ------------------------------------------------------------------------------
-- Question 3: What is the absolute maximum passenger arrival rate recorded 
-- at each station in a single hour?
-- ------------------------------------------------------------------------------
SELECT 
    station_name, 
    ROUND(MAX(arrival_rate_per_min)) AS max_peak_arrival_rate_per_min
FROM 
    processed_mrt3_ridership
WHERE 
    action = 'entry'
GROUP BY 
    station_name
ORDER BY 
    max_peak_arrival_rate_per_min DESC;