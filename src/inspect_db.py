import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://dss150p:dss150p_lab@localhost:5432/dss150p_lab")

print("=== Tables in Database ===")
tables = pd.read_sql("""
SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_schema NOT IN ('pg_catalog', 'information_schema');
""", engine)
print(tables)

for _, row in tables.iterrows():
    schema, table_name = row['table_schema'], row['table_name']
    qualified = f"{schema}.{table_name}"
    print(f"\n=== Inspecting Table: {qualified} ===")

    print("\n--- Columns and Data Types ---")
    cols = pd.read_sql(f"""
    SELECT column_name, data_type, is_nullable
    FROM information_schema.columns
    WHERE table_schema = '{schema}' AND table_name = '{table_name}'
    ORDER BY ordinal_position;
    """, engine)
    print(cols.to_string(index=False))

    print("\n--- Constraints/Keys ---")
    keys = pd.read_sql(f"""
    SELECT tc.constraint_type, kcu.column_name
    FROM information_schema.table_constraints tc
    JOIN information_schema.key_column_usage kcu
      ON tc.constraint_name = kcu.constraint_name
    WHERE tc.table_schema = '{schema}' AND tc.table_name = '{table_name}';
    """, engine)
    print(keys.to_string(index=False) if not keys.empty else "(none)")

    print("\n--- Row Count ---")
    count = pd.read_sql(f"SELECT COUNT(*) FROM {qualified};", engine)
    print(f"Total rows: {count.iloc[0,0]}")

    print("\n--- Top 5 Sample Rows ---")
    sample = pd.read_sql(f"SELECT * FROM {qualified} LIMIT 5;", engine)
    print(sample.to_string(index=False))

if tables.empty:
    print("\nNo tables found! The database is currently empty.")
