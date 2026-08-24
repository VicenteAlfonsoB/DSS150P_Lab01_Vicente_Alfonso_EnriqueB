import pandas as pd
import os
from pathlib import Path

RAW = Path("data/raw")

# Load datasets safely
datasets = {}
try: datasets["customers.csv"] = pd.read_csv(RAW / "customers.csv")
except FileNotFoundError: print("Missing: customers.csv")

try: datasets["orders.json"] = pd.read_json(RAW / "orders.json")
except FileNotFoundError: print("Missing: orders.json")

try: datasets["products.parquet"] = pd.read_parquet(RAW / "products.parquet")
except FileNotFoundError: print("Missing: products.parquet")

# Profile each dataset
for name, df in datasets.items():
    print(f"\n" + "="*50)
    print(f"=== Profiling: {name} ===")
    print("="*50)
    
    file_path = RAW / name
    print(f"File Size: {os.path.getsize(file_path) / 1024:.2f} KB")
    print(f"Shape (Rows, Columns): {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"Column Names: {list(df.columns)}")
    
    print("\n--- Data Types ---")
    print(df.dtypes)
    
    print("\n--- Missing/Null Values ---")
    print(df.isna().sum())
    
    print(f"\nFully Duplicated Rows: {df.duplicated().sum()}")
    
    print("\n--- Distinct Values per Column ---")
    print(df.nunique())
    
    # Min/Max for Numeric Columns
    numeric_cols = df.select_dtypes(include='number').columns
    if not numeric_cols.empty:
        print("\n--- Numeric Columns (Min/Max) ---")
        for col in numeric_cols:
            print(f"  {col}: Min = {df[col].min()}, Max = {df[col].max()}")
            
    # Earliest/Latest for Datetime Columns
    datetime_cols = df.select_dtypes(include='datetime').columns
    if not datetime_cols.empty:
        print("\n--- Datetime Columns (Earliest/Latest) ---")
        for col in datetime_cols:
            print(f"  {col}: Earliest = {df[col].min()}, Latest = {df[col].max()}")
            
    print("\n--- First 5 Records ---")
    print(df.head())
    print("\n")
