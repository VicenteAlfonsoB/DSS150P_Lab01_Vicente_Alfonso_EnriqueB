import pandas as pd
import os
from pathlib import Path

RAW = Path("data/raw")

datasets = {}
try: datasets["customers.csv"] = pd.read_csv(RAW / "customers.csv")
except FileNotFoundError: print("Missing: customers.csv")

try: datasets["orders.json"] = pd.read_json(RAW / "orders.json")
except FileNotFoundError: print("Missing: orders.json")

try: datasets["products.parquet"] = pd.read_parquet(RAW / "products.parquet")
except FileNotFoundError: print("Missing: products.parquet")

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

    # nested dict/list columns are unhashable, stringify before comparing rows
    flat = df.copy()
    for col in flat.columns:
        if flat[col].apply(lambda v: isinstance(v, (dict, list))).any():
            flat[col] = flat[col].astype(str)

    print(f"\nFully Duplicated Rows: {flat.duplicated().sum()}")

    print("\n--- Distinct Values per Column ---")
    print(flat.nunique())

    numeric_cols = df.select_dtypes(include='number').columns
    if not numeric_cols.empty:
        print("\n--- Numeric Columns (Min/Max) ---")
        for col in numeric_cols:
            print(f"  {col}: Min = {df[col].min()}, Max = {df[col].max()}")

    print("\n--- Date/Time Columns (Earliest/Latest, after safe parsing) ---")
    found_dates = False
    for col in df.columns:
        if df[col].dtype == 'datetime64[ns]' or any(k in col.lower() for k in ('date', 'time', '_at')):
            parsed = pd.to_datetime(df[col], errors='coerce')
            if parsed.notna().any():
                found_dates = True
                print(f"  {col}: Earliest = {parsed.min()}, Latest = {parsed.max()}")
    if not found_dates:
        print("  (none detected)")

    print("\n--- First 5 Records ---")
    print(df.head())
    print("\n")
