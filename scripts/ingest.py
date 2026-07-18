import shutil
from pathlib import Path

# Ensure the target directory exists
RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

def main():
    # The raw file provided by the DOTr eFOI portal
    source_name = "Leandra Oania.xlsx"
    source_path = Path(source_name)
    
    # Standardizing the filename for our pipeline
    output_file = RAW_DIR / "mrt3_hourly_ridership_2026_raw.xlsx"
    
    print(f"Initiating data ingestion for: {source_name}...")
    
    try:
        # Check if the file is actually in the folder
        if not source_path.exists():
            print(f"Error: Could not find '{source_name}'. Please ensure it is in the root project folder.")
            return

        # Safely copy the raw dataset into /data/raw
        shutil.copy2(source_path, output_file)
        
        print(f"Success! Standardized and saved raw data to {output_file}")
        
    except Exception as e:
        print(f"Ingestion failed: {e}")

if __name__ == "__main__":
    main()