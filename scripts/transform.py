from pathlib import Path
import pandas as pd
import numpy as np

# Define input and output paths
RAW_FILE = Path("Leandra Oania.xlsx")
OUTPUT_FILE = Path("data/processed/processed_mrt3_ridership.csv")

def main():
    print(f"Loading raw data from {RAW_FILE}...")
    
    # 1. Load the data, skipping the messy header rows
    df = pd.read_excel(RAW_FILE, skiprows=5)
    
    # 2. Extract and rename the core columns
    clean_columns = [
        "date", "time_interval", 
        "north_ave_entry", "north_ave_exit",
        "quezon_ave_entry", "quezon_ave_exit",
        "gma_kamuning_entry", "gma_kamuning_exit",
        "cubao_entry", "cubao_exit",
        "santolan_entry", "santolan_exit",
        "ortigas_entry", "ortigas_exit"
    ]
    df_cleaned = df.iloc[:, :14].copy() 
    df_cleaned.columns = clean_columns
    
    # 3. Explicit Cleaning Logic (Milestone 2 Requirement)
    print("\nApplying data cleaning rules...")
    
    # Drop the first row which contains leftover string headers
    df_cleaned = df_cleaned.drop(0)
    
    # Handle Nulls: Drop rows where there is no date (these are empty spreadsheet rows)
    df_cleaned = df_cleaned.dropna(subset=['date'])
    
    # Forward fill the date column (because the Excel file only lists the date once per day)
    df_cleaned['date'] = df_cleaned['date'].ffill()
    
    # Ensure Date is actually a datetime object
    df_cleaned['date'] = pd.to_datetime(df_cleaned['date'], errors='coerce')
    
    # 4. Transform from Wide to Long Format (Unpivot)
    print("Unpivoting data into analysis-ready long format...")
    
    # We use melt to turn the station columns into rows
    df_long = pd.melt(
        df_cleaned, 
        id_vars=['date', 'time_interval'],
        var_name='station_action', 
        value_name='passenger_count'
    )
    
    # Split the 'station_action' column into separate 'station_name' and 'action' (entry/exit) columns
    df_long[['station_name', 'action']] = df_long['station_action'].str.rsplit('_', n=1, expand=True)
    df_long = df_long.drop(columns=['station_action'])
    
    # Ensure passenger counts are integers, filling any missing hour gaps with 0
    df_long['passenger_count'] = pd.to_numeric(df_long['passenger_count'], errors='coerce').fillna(0).astype(int)
    
    # 5. Calculate Derived Metrics
    print("Calculating arrival_rate_per_min for simulation inputs...")
    
    # Only calculate the arrival rate for entry actions (passengers arriving at the platform)
    df_long['arrival_rate_per_min'] = np.where(
        df_long['action'] == 'entry',
        df_long['passenger_count'] / 60.0,
        0.0
    )

    # ---------------------------------------------------------
    # NEW CODE TO INSERT: Step 5.5 - Validation Checks
    # ---------------------------------------------------------
    print("Running validation checks...")
    
    # Check 1: No missing values in our primary composite key
    assert df_long['date'].isna().sum() == 0, "Validation Failed: Nulls found in 'date' column."
    assert df_long['time_interval'].isna().sum() == 0, "Validation Failed: Nulls found in 'time_interval' column."
    assert df_long['station_name'].isna().sum() == 0, "Validation Failed: Nulls found in 'station_name' column."
    
    # Check 2: Passenger counts should never be negative
    assert df_long['passenger_count'].min() >= 0, "Validation Failed: Negative passenger count detected."
    
    # Check 3: Arrival rate should never be negative
    assert df_long['arrival_rate_per_min'].min() >= 0, "Validation Failed: Negative arrival rate detected."
    
    print("All validation checks passed!")
    
    # ---------------------------------------------------------

    # 6. Save the Final Analysis-Ready Dataset
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df_long.to_csv(OUTPUT_FILE, index=False)
    print(f"\nSuccess! Saved analysis-ready dataset to {OUTPUT_FILE}")
    print("\n--- Final Dataset Preview ---")
    print(df_long.head())

if __name__ == "__main__":
    main()