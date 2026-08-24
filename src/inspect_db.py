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

if not tables.empty:
    table_name = tables.iloc[0]['table_name']
    print(f"\n=== Inspecting Table: {table_name} ===")

    print("\n--- Columns and Data Types ---")
    cols = pd.read_sql(f"""
    SELECT column_name, data_type, is_nullable
    FROM information_schema.columns
    WHERE table_name = '{table_name}'
    ORDER BY ordinal_position;
    """, engine)
    print(cols.to_string(index=False))

    print("\n--- Row Count ---")
    count = pd.read_sql(f"SELECT COUNT(*) FROM {table_name};", engine)
    print(f"Total rows: {count.iloc[0,0]}")

    print("\n--- Top 5 Sample Rows ---")
    sample = pd.read_sql(f"SELECT * FROM {table_name} LIMIT 5;", engine)
    print(sample.to_string(index=False))
else:
    print("\nNo tables found! The database is currently empty.")
