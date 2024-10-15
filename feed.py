import json
import requests

# Read the data from the file
with open('mocks.json', 'r') as f:
    data = json.load(f)

bulk_data = ""
for doc in data:
    print(doc)  # Debug: Print the current document
    doc_id = doc.get('id')
    if doc_id is not None:  # Only process documents with an 'id'
        bulk_data += json.dumps({ "index": { "_index": "my_index", "_id": doc_id }}) + "\n"
        bulk_data += json.dumps(doc) + "\n"
    else:
        print(f"Document missing 'id': {doc}")  # Debugging missing id

# Send the data to Elasticsearch
response = requests.post('http://localhost:9200/_bulk', headers={'Content-Type': 'application/json'}, data=bulk_data)

# Print response from Elasticsearch
print(response.json())
