from flask import Flask, request, jsonify, render_template
from elasticsearch import Elasticsearch
import json

app = Flask(__name__)
es = Elasticsearch("http://localhost:9201", http_auth=('elastic', 'JyzOSl9yte-f7PgXTk+v'))

# Load data from mocks.json into Elasticsearch
def load_initial_data():
    # Make sure to run this function only once to avoid duplicating documents
    if es.indices.exists(index='codex-10-14-2024'):
        print("Index already exists. Skipping data load.")
        return

    with open('mocks_es_format.json') as f:
        data = json.load(f)
        for item in data:
            es.index(index='codex-10-14-2024', body=item)
    print("Initial data loaded successfully.")

# Serve the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Save a document
@app.route('/document', methods=['POST'])
def create_document():
    document = request.json.get('document')
    response = es.index(index='codex-10-14-2024', body=document)
    document_id = response['_id']
    
    return jsonify({
        'document': {
            'id': document_id,
            'title': document.get('title'),
            'content': document.get('content')
        }
    }), 201

# Search for documents
@app.route('/search', methods=['GET'])
def search():
    query_string = request.args.get('querystring', '')
    print(f"Search Query: {query_string}")  # Log the query string
    #ELASTICSEARCH
    body = {
        "query": {
            "bool": {
                "should": [
                    {
                        "match": {
                            "title": {
                                "query": query_string,
                                "fuzziness": "AUTO",  # Allows fuzzy matching for typos
                                "boost": 2,  # Boost title matches
                                "minimum_should_match": "75%"  # Requires 75% match of terms
                            }
                        }
                    },
                    {
                        "match": {
                            "content": {
                                "query": query_string,
                                "fuzziness": "AUTO",  # Fuzziness for content
                                "minimum_should_match": "75%"
                            }
                        }
                    }
                ]
            }
        }
    }

    
    print("Elasticsearch Query Body:", json.dumps(body, indent=2))  # Log the query body

    res = es.search(index="codex-10-14-2024", body=body)

    documents = []
    for hit in res['hits']['hits']:
        if query_string.lower() in hit['_source']['title'].lower():
            documents.append({
                "id": hit['_id'],
                "fieldName": 'title',
                "fieldContent": hit['_source']['title'],
            })
        elif query_string.lower() in hit['_source']['content'].lower():
            documents.append({
                "id": hit['_id'],
                "fieldName": 'content',
                "fieldContent": hit['_source']['content'],
            })

    return jsonify({"documents": documents})

# Patch a document
@app.route('/document', methods=['PATCH'])
def patch_document():
    document_id = request.json.get('documentId')
    updated_document = request.json.get('document')
    
    es.update(index='codex-10-14-2024', id=document_id, body={"doc": updated_document})
    
    return jsonify({
        'document': {
            'id': document_id,
            'title': updated_document.get('title'),
            'content': updated_document.get('content')
        }
    }), 200

if __name__ == '__main__':
    # Load initial data from mocks.json if you haven't already done so
    load_initial_data()
    
    app.run(debug=True)
