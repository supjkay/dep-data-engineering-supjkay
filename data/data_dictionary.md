# Data Dictionary: MRT-3 Hourly Ridership (Raw)

**File:** `mrt3_hourly_ridership_2026_raw.xlsx`  
**Source:** DOTr eFOI Portal  
**Description:** Hourly passenger entry and exit counts for all 13 MRT-3 stations. 

*Note: The raw Excel file contains a multi-level header spanning rows 6 and 7. The logical schema below describes the parsed data structure.*

| Field Name | Data Type | Description |
| :--- | :--- | :--- |
| `Date` | Datetime | The specific date of the ridership record (Format: YYYY-MM-DD). Found in the first column. |
| `Time` | String | The 1-hour interval for the ridership count (e.g., "06:00 - 06:59"). Found in the second column. |
| `[Station_Name]_Entry` | Integer | The total number of passengers who entered the specific station during the time interval. There is one entry column for each of the 13 stations (e.g., `North_Ave_Entry`, `Taft_Entry`). |
| `[Station_Name]_Exit` | Integer | The total number of passengers who exited the specific station during the time interval. There is one exit column for each of the 13 stations. |
| `Total_Entry` | Integer | The aggregate sum of all passenger entries across all 13 stations during the time interval. |
| `Total_Exit` | Integer | The aggregate sum of all passenger exits across all 13 stations during the time interval. |

## Station List Reference
The following 13 stations are tracked sequentially in the dataset (North to South):
1. North Ave
2. Quezon Ave
3. GMA Kamuning
4. Cubao
5. Santolan
6. Ortigas
7. Shaw Blvd
8. Boni Ave
9. Guadalupe
10. Buendia
11. Ayala Ave
12. Magallanes
13. Taft