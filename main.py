from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2
from elasticsearch import Elasticsearch

app = FastAPI()

# Set up PostgreSQL connection
conn = psycopg2.connect(
    dbname="mydb", user="myuser", password="mypassword", host="localhost"
)
cursor = conn.cursor()

# Set up Elasticsearch connection
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Pydantic model for document input
class DocumentInput(BaseModel):
    title: str
    content: str

# Pydantic model for document response
class DocumentResponse(BaseModel):
    id: int
    title: str
    content: str


# Route to save a document (POST /document)
@app.post("/document", response_model=DocumentResponse)
def save_document(document: DocumentInput):
    try:
        # Insert into PostgreSQL and get document ID
        cursor.execute(
            "INSERT INTO documents (title, content) VALUES (%s, %s) RETURNING id",
            (document.title, document.content)
        )
        doc_id = cursor.fetchone()[0]
        conn.commit()

        # Index document in Elasticsearch
        es.index(index="documents", id=doc_id, body=document.dict())
        
        return {"id": doc_id, "title": document.title, "content": document.content}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))


# Route to search for a substring in documents (GET /document/search)
@app.get("/document/search")
def search_documents(query: str):
    try:
        # Perform full-text search in Elasticsearch with priority to the title field
        search_body = {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["title^2", "content"]  # title has higher priority
                }
            }
        }
        results = es.search(index="documents", body=search_body)

        # Prepare response
        search_results = []
        for hit in results['hits']['hits']:
            doc_id = hit['_id']
            source = hit['_source']
            field_name = "title" if query.lower() in source['title'].lower() else "content"
            field_content = source[field_name]
            
            search_results.append({
                "id": doc_id,
                "fieldName": field_name,
                "fieldContent": field_content
            })
        
        return search_results

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
