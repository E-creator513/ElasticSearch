import json
from elasticsearch import Elasticsearch

# Initialize Elasticsearch client with the 'scheme' parameter
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])

# Load the JSON file
with open('C:/Users/User/Downloads/backend/mocks.json', 'r') as file:
    data = json.load(file)

# Index name
index_name = 'temp_json_data'

# Insert each JSON object into Elasticsearch
for item in data:
    # Generate a unique ID for each document (optional)
    doc_id = item.get('id', None) or item['title'].lower().replace(' ', '_')
    
    # Index the document
    es.index(index=index_name, id=doc_id, body=item)

print("Data inserted into Elasticsearch successfully.")