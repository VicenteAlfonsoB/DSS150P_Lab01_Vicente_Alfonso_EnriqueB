# DSS150P — Laboratory Activity #1
**Reproducible Data-Engineering Workspace and Source Assessment**

- **Name:** Alfonso Enrique B. Vicente
- **Student Number:** <YOUR STUDENT NUMBER HERE>
- **Section:** <YOUR SECTION HERE>

## Purpose of the Laboratory
Set up a reproducible local data-engineering environment (Python, Git, Docker, PostgreSQL) and perform a first-pass technical assessment of several source systems: a CSV file, a JSON file, a Parquet file, a REST API, and a PostgreSQL table. The output is a documented understanding of each source's structure, schema, metadata, and acquisition requirements, plus a basic relational schema and data contract for one selected source.

## Software Requirements
- Python 3.x (tested with Python 3.13.9)
- Git (tested with 2.50.1)
- Docker Desktop with Docker Compose (tested with Docker 29.7.2 / Compose v5.4.0)
- A code editor (Visual Studio Code)
- Internet access for the instructor-provided REST API and package installation

## Reproducing the Environment
```bash
# 1. Clone the repository and enter it
git clone https://github.com/VicenteAlfonsoB/DSS150P_Lab01_Vicente_Alfonso_Enrique_B.git
cd DSS150P_Lab01_Vicente_Alfonso_Enrique_B

# 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .\.venv\Scripts\Activate.ps1   # Windows PowerShell

# 3. Install dependencies
pip install -r requirements.txt
```

## Starting and Stopping PostgreSQL
```bash
# Start (detached)
docker compose up -d

# Confirm the container is running
docker ps

# Stop (keeps data in the named volume)
docker compose down
```
The database uses a local development password only (defined in `docker-compose.yml`); no personal or production credentials are used.

## Running the Python Scripts
Run all scripts from the repository root with the virtual environment activated:
```bash
python src/verify_environment.py   # connects to PostgreSQL, prints version + current database
python src/profile_sources.py      # profiles data/raw/customers.csv, orders.json, products.parquet
python src/inspect_api.py          # fetches the REST API, saves data/raw/api_snapshot.json
python src/inspect_db.py           # inspects PostgreSQL table metadata and sample rows
```
To apply the lab schema:
```bash
docker exec -i dss150p-postgres psql -U dss150p -d dss150p_lab < sql/01_create_schema.sql
```

## Description of Each Source
| Source | Format | Notes |
| --- | --- | --- |
| `data/raw/customers.csv` | CSV (structured) | Customer entity data; candidate key `customer_id`. |
| `data/raw/orders.json` | JSON (semi-structured) | Order records; candidate key `order_id`; possible nested fields. |
| `data/raw/products.parquet` | Parquet (structured, columnar) | Product data with an embedded schema. |
| REST API (instructor-provided) | JSON over HTTP | Snapshot saved to `data/raw/api_snapshot.json`; retrieval timestamp recorded in `docs/source_inventory.md`. |
| PostgreSQL (`dss150p_lab`) | Relational tables | Dockerized Postgres 16; schema and metadata documented in `data/evidence/db_profile.txt`. |

Full details are in `docs/source_inventory.md` and `docs/source_profile.md`.

## Known Limitations / Unresolved Questions
- The true business owner and freshness expectations of `customers.csv` are unknown and require confirmation from the source owner (see `docs/data_contract.yaml`).
- The raw files are profiled as-is; no transformation or bulk loading has been performed (out of scope for this lab).
- <ADD ANY OTHER LIMITATIONS YOU OBSERVED>

## AI Usage
I used Claude Code (Anthropic) as a refresher on the basics while completing, helped me debug script errors (nested JSON columns in pandas, schema-qualified SQL queries), and helped structure my documentation. I set up the environment, ran all scripts myself, reviewed every change, and wrote the reflection and source profile interpretations in my own words. I can explain and reproduce each step.
