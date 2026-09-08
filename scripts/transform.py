from pathlib import Path
import pandas as pd

# Define input and output paths
RAW_FILE = Path("Leandra Oania.xlsx")
OUTPUT_FILE = Path("data/processed/processed_mrt3_ridership.csv")

def main():
    print(f"Loading raw data from {RAW_FILE}...")
    
    # The actual data headers are on rows 5 and 6 (index 5 and 6). 
    # We skip the first 5 rows to make row 6 the header.
    df = pd.read_excel(RAW_FILE, skiprows=5)
    
    # Basic profiling required by M2
    print("\n--- Data Profiling (First 5 Rows) ---")
    print(df.head())
    
    print("\n--- Data Profiling (Info) ---")
    print(df.info())

    # --- Basic Column Cleanup ---
    # The columns are messy because of the merged cells in Excel. 
    # Let's give them clean, standardized names for the first 14 columns as an initial pass.
    # We will rename the Date, Time, and the Entry/Exit for the first few stations.
    
    clean_columns = [
        "date", "time_interval", 
        "north_ave_entry", "north_ave_exit",
        "quezon_ave_entry", "quezon_ave_exit",
        "gma_kamuning_entry", "gma_kamuning_exit",
        "cubao_entry", "cubao_exit",
        "santolan_entry", "santolan_exit",
        "ortigas_entry", "ortigas_exit"
    ]
    
    # We'll just grab the first 14 columns to match our clean names for this first version
    df_cleaned = df.iloc[:, :14].copy() 
    df_cleaned.columns = clean_columns
    
    # Drop the first row which contains the leftover "Entry/Exit" strings from the raw file
    df_cleaned = df_cleaned.drop(0)

    # Save to /data/processed/
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df_cleaned.to_csv(OUTPUT_FILE, index=False)
    print(f"\nSaved first cleaned dataset version to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()