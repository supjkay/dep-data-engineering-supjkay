import pandas as pd
import sqlite3
from pathlib import Path

def main():
    csv_path = Path("data/processed/processed_mrt3_ridership.csv")
    sql_path = Path("scripts/business_questions.sql")

    print("1. Loading processed dataset into memory...")
    df = pd.read_csv(csv_path)

    # Create a temporary in-memory SQLite database
    conn = sqlite3.connect(":memory:")
    
    # Push the dataframe into a SQL table named exactly what your queries expect
    df.to_sql("processed_mrt3_ridership", conn, index=False)
    print("2. Database ready. Executing SQL queries...\n")
    
    # Read the SQL file
    with open(sql_path, "r") as file:
        sql_script = file.read()

    # Split the file by semicolons so we can run each query individually
    queries = sql_script.split(';')
    
    query_num = 1
    for query in queries:
        if query.strip():
            print(f"--- Business Question {query_num} Results ---")
            try:
                # Run the SQL query and print the result
                result_df = pd.read_sql_query(query, conn)
                print(result_df.to_string(index=False))
                print("\n" + "="*50 + "\n")
            except Exception as e:
                print(f"Error running query: {e}")
            query_num += 1

    conn.close()

if __name__ == "__main__":
    main()