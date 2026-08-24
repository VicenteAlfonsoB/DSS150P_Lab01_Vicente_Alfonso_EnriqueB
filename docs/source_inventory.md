# Source Inventory

## 1. customers.csv
* **Source name:** customers.csv
* **Source-system type:** Flat File
* **Data format:** CSV
* **Structured / semi-structured / unstructured:** Structured
* **Expected update pattern:** Batch / Daily
* **Likely acquisition method:** Batch ingestion via Python (Pandas)
* **Schema location or schema owner:** Local file system / Analytics Team
* **Possible primary/business key:** customer_id
* **Potential schema-evolution risk:** Columns might be added, removed, or reordered without warning.
* **Potential data-quality risk:** Missing values (nulls) or duplicate rows.

## 2. orders.json
* **Source name:** orders.json
* **Source-system type:** Document / NoSQL Export
* **Data format:** JSON
* **Structured / semi-structured / unstructured:** Semi-structured
* **Expected update pattern:** Real-time or micro-batch
* **Likely acquisition method:** API or event stream ingestion
* **Schema location or schema owner:** Local file system / Application Team
* **Possible primary/business key:** order_id
* **Potential schema-evolution risk:** Nested fields might change or keys might be missing entirely.
* **Potential data-quality risk:** Inconsistent data types within the same field across different JSON objects.

## 3. products.parquet
* **Source name:** products.parquet
* **Source-system type:** Columnar Storage / Data Lake
* **Data format:** Parquet
* **Structured / semi-structured / unstructured:** Structured
* **Expected update pattern:** Batch / Periodic
* **Likely acquisition method:** Direct read from file path using PyArrow/Pandas
* **Schema location or schema owner:** Embedded in the file / Data Engineering
* **Possible primary/business key:** product_id
* **Potential schema-evolution risk:** Data type changes that violate the strict Parquet schema.
* **Potential data-quality risk:** Corrupted file metadata or missing partitions.

## 4. REST API
* **Source name:** Instructor-provided REST API
* **Source-system type:** Web Service
* **Data format:** JSON
* **Structured / semi-structured / unstructured:** Semi-structured
* **Expected update pattern:** Real-time / On-demand
* **Likely acquisition method:** HTTP GET requests using Python `requests` library
* **Schema location or schema owner:** External Provider / Instructor
* **Possible primary/business key:** id (or equivalent unique identifier in the payload)
* **Potential schema-evolution risk:** The endpoint URL might change, or the API version could be deprecated.
* **Potential data-quality risk:** Network timeouts, rate limiting, or receiving unexpected HTTP error codes (e.g., 500, 404).
* **API Retrieval Timestamp (UTC):** 2026-08-24T14:48:24Z

## 5. PostgreSQL Database
* **Source name:** dss150p_lab (Dockerized PostgreSQL 16 instance)
* **Source-system type:** Relational Database (OLTP)
* **Data format:** Relational tables (SQL)
* **Structured / semi-structured / unstructured:** Structured
* **Expected update pattern:** Transactional / Continuous inserts and updates
* **Likely acquisition method:** SQL queries over a database connection (SQLAlchemy/psycopg2), or batch extracts
* **Schema location or schema owner:** Defined in the database catalog (`information_schema`) / Database Administrator
* **Possible primary/business key:** customer_id (declared PRIMARY KEY in the table definition)
* **Potential schema-evolution risk:** Columns altered or dropped by migrations without notifying downstream consumers.
* **Potential data-quality risk:** Constraint violations if checks are disabled, or stale data if the snapshot is not refreshed.
