from flask import Flask, request, jsonify, render_template
from elasticsearch import Elasticsearch
import json

app = Flask(__name__)
es = Elasticsearch("http://localhost:9201", http_auth=('elastic', 'JyzOSl9yte-f7PgXTk+v'))

INDEX_NAME = 'codex-10-22-2024'  # the index name is consistent

# Load data from mocks_es_format.json into Elasticsearch
def load_initial_data():
    # Check index already exists
    if es.indices.exists(index=INDEX_NAME):
        print("Index already exists. Skipping data load.")
        return

    try:
        with open('updated_mocks_es_format.json') as f:
            data = json.load(f)
            for item in data:
                es.index(index=INDEX_NAME, body=item)
        print("Initial data loaded successfully.")
    except Exception as e:
        print(f"Error loading initial data: {e}")

# Serve the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Save a document
@app.route('/document', methods=['POST'])
def create_document():
    document = request.json.get('document')
    response = es.index(index=INDEX_NAME, body=document)
    document_id = response['_id']
    
    return jsonify({
        'document': {
            'id': document_id,
            'title': document.get('title'),
            'content': document.get('content')
        }
    }), 201

@app.route('/search', methods=['GET'])
def search():
    query_string = request.args.get('querystring', '')
    print(f"Search Query: {query_string}")  # Log the query string
    
    body = {
        "query": {
            "multi_match": {
                "query": query_string,
                "fields": ["title^2", "content"],  # Boost title matches
                "fuzziness": "AUTO",  # Allows fuzzy matching for typos
                "minimum_should_match": "75%"
            }
        }
    }

    print("Elasticsearch Query Body:", json.dumps(body, indent=2))  # Log the query body

    try:
        res = es.search(index=INDEX_NAME, body=body)

        documents = [
            {
                "id": hit['_id'],
                "fieldName": 'title' if 'title' in hit['_source'] else 'content',
                "fieldContent": hit['_source'].get('title', hit['_source'].get('content', ''))
            }
            for hit in res['hits']['hits']
        ]

        return jsonify({"documents": documents})

    except Exception as e:
        print(f"Error during search: {e}")
        return jsonify({"error": "Search failed"}), 500

# Patch a document
@app.route('/document', methods=['PATCH'])
def patch_document():
    document_id = request.json.get('documentId')
    updated_document = request.json.get('document')
    
    try:
        es.update(index=INDEX_NAME, id=document_id, body={"doc": updated_document})
        return jsonify({
            'document': {
                'id': document_id,
                'title': updated_document.get('title'),
                'content': updated_document.get('content')
            }
        }), 200
    except Exception as e:
        print(f"Error updating document: {e}")
        return jsonify({"error": "Document update failed"}), 500

if __name__ == '__main__':
    # Load initial data from mocks.json if you haven't already done so
    load_initial_data()
    
    app.run(debug=True)
