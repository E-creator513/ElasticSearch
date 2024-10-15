import psycopg2
from elasticsearch import Elasticsearch

# PostgreSQL database connection parameters
db_params = {
    'dbname': 'mock_json_db',
    'user': 'postgres',
    'password': '0125',
    'host': 'localhost',
    'port': '5432'
}

# Initialize Elasticsearch client
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])

# Connect to the PostgreSQL database
conn = psycopg2.connect(**db_params)
cur = conn.cursor()

# Retrieve documents from PostgreSQL
cur.execute("SELECT * FROM documents")
rows = cur.fetchall()

# Index each document into Elasticsearch
for row in rows:
    doc_id, title, content = row  # Adjust based on your table's structure
    es.index(index='documents', id=doc_id, body={'title': title, 'content': content})

# Close the database connection
cur.close()
conn.close()
