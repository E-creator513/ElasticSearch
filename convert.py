import json

# Load the JSON data from mocks.json
with open("mocks.json") as f:
    data = json.load(f)

# Create the action metadata and the bulk payload
bulk_data = []

for idx, item in enumerate(data, start=1):  # Start IDs from 1
    action_metadata = {"index": {"_index": "your_index_name", "_id": str(idx)}}
    document = {
        "title": item["title"],
        "content": item["content"]
    }
    # Append action metadata and document with newlines
    bulk_data.append(json.dumps(action_metadata) + "\n")  # Add action metadata to bulk data with newline
    bulk_data.append(json.dumps(document) + "\n")  # Add the actual document to bulk data with newline

# Write to a file
with open("mocks_es_format.json", "w") as f:
    f.writelines(bulk_data)  # Use writelines to write all lines at once

print("Conversion complete. Check mocks_es_format.json for the output.")
