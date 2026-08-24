# Data Engineering Lifecycle Map

## Lifecycle Table

| Lifecycle Element | What It Means | Example in This Lab | Primary Tool/Artifact | Possible Failure |
| :--- | :--- | :--- | :--- | :--- |
| **Source system** | The origin point where raw data is created or currently resides. | The REST API, `customers.csv`, `orders.json`, and `products.parquet`. | External API / Local Files | The API endpoint goes offline, or a file gets corrupted. |
| **Ingestion/acquisition** | The process of connecting to sources and bringing data into our environment. | Reading the CSV/JSON/Parquet files and requesting API data. | Python (`pandas`, `requests`) | Network timeout during API call, or missing file paths. |
| **Storage** | The systems used to hold data reliably for future use or processing. | The local database we set up. | PostgreSQL (via Docker) | The Docker container crashes, or local disk runs out of space. |
| **Processing/transformation** | Cleaning, joining, and structuring raw data into a usable format. | (Future step) Converting the raw JSON/CSV into relational tables. | Python / SQL | Data type mismatch (e.g., trying to parse text as a date). |
| **Data quality/validation** | Checking data for accuracy, completeness, and reliability. | Profiling the sources to check for nulls and duplicates. | Python (`pandas`) | Finding unexpected null values in a primary key column. |
| **Delivery** | Making the processed data available and accessible to end-users. | Providing access to the structured PostgreSQL database schema. | PostgreSQL | Access denied due to incorrect database credentials. |
| **Consumer** | The end-user or system that uses the data for analysis or products. | The fictional analytics team or downstream analyst. | BI Tools / Jupyter Notebooks | The analyst misinterprets the meaning of a specific column. |

## Data Flow Diagram

Below is a simple box-and-arrow diagram showing how the supplied sources flow toward the consumer:

```mermaid
graph TD
    %% Sources
    A1[CSV Source: customers.csv] --> B
    A2[JSON Source: orders.json] --> B
    A3[Parquet Source: products.parquet] --> B
    A4[REST API Endpoint] --> B

    %% Ingestion/Processing
    B[Pipeline/Process Box: Python Script] --> C

    %% Storage
    C[(Storage/Destination Box: PostgreSQL Database)] --> D

    %% Consumer
    D[Downstream Analyst / Application Consumer]

