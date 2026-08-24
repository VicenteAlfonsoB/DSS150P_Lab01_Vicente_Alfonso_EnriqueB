import json
from datetime import datetime, timezone
import requests

# Using a standard test API since the LMS one is missing
API_URL = "https://jsonplaceholder.typicode.com/users"

# 1 & 2: Send GET request with a 20-second timeout
response = requests.get(API_URL, timeout=20)

# 3: Check HTTP status code and fail if unsuccessful
response.raise_for_status()

# 4: Print Content-Type header
print("status:", response.status_code)
print("content-type:", response.headers.get("Content-Type"))

# 5 & 6: Parse JSON and determine top-level structure
payload = response.json()
print("top-level type:", type(payload).__name__)

# 7 & 8: Print number of records and a sample record
if isinstance(payload, list):
    print("number of records:", len(payload))
    if len(payload) > 0:
        print("sample record:", json.dumps(payload[0], indent=2))

# 9: Save raw response exactly as received
with open("data/raw/api_snapshot.json", "w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2, ensure_ascii=False)

# 10: Generate retrieval timestamp in UTC
print("retrieved_at_utc:", datetime.now(timezone.utc).isoformat())
