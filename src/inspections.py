from pathlib import Path
import pandas as pd

# Put this script beside the CSV files.
folder = Path("data/raw")

files = [
    "T1_1_Population.csv", 
    "T9_14_Practitioners.csv",
    "T9_17_Beds.csv", 
    "T9_18_Hospitals.csv",
    "T9_19_Health_stations.csv"
]

for filename in files:
    df = pd.read_csv(folder / filename)
    print(f"\n--- {filename} ---")
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print("\nSample:")
    print(df.head().to_string(index=False))
    print("\nData types:")
    print(df.dtypes.to_string())
    print("\nMissing cells by column:")
    print(df.isna().sum().to_string())
    print("\nDuplicate rows:", df.duplicated().sum())
