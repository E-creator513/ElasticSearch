curl -X PUT "http://localhost:9201/codex-10-14-2024" -H "Content-Type: application/json" -u elastic:JyzOSl9yte-f7PgXTk+v -d '{
  "settings": {
    "analysis": {
      "filter": {
        "autocomplete_filter": {
          "type": "edge_ngram",
          "min_gram": 2,
          "max_gram": 20
        },
        "stemmer_filter": {
          "type": "stemmer",
          "language": "english"
        },
        "synonym_filter": {
          "type": "synonym",
          "synonyms": [
            "run, running",
            "jump, jumping",
            "walk, walking"
          ]
        }
      },
      "analyzer": {
        "autocomplete_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "autocomplete_filter"
          ]
        },
        "stemmed_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "stemmer_filter"
          ]
        },
        "synonym_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "synonym_filter"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "title": {
        "type": "text",
        "analyzer": "autocomplete_analyzer",
        "search_analyzer": "standard"
      },
      "description": {
        "type": "text",
        "analyzer": "stemmed_analyzer",
        "search_analyzer": "standard"
      },
      "tags": {
        "type": "text",
        "analyzer": "synonym_analyzer",
        "search_analyzer": "standard"
      }
    }
  }
}'

curl -X POST "http://localhost:9201/codex-10-14-2024/_close" -H "Content-Type: application/json" -u elastic:JyzOSl9yte-f7PgXTk+v


curl -X PUT "http://localhost:9201/codex-10-14-2024/_settings" -H "Content-Type: application/json" -u elastic:JyzOSl9yte-f7PgXTk+v -d '{
  "analysis": {
    "filter": {
      "autocomplete_filter": {
        "type": "edge_ngram",
        "min_gram": 2,
        "max_gram": 20
      },
      "stemmer_filter": {
        "type": "stemmer",
        "language": "english"
      },
      "synonym_filter": {
        "type": "synonym",
        "synonyms": [
          "run, running",
          "jump, jumping",
          "walk, walking"
        ]
      }
    },
    "analyzer": {
      "autocomplete_analyzer": {
        "type": "custom",
        "tokenizer": "standard",
        "filter": [
          "lowercase",
          "autocomplete_filter"
        ]
      },
      "stemmed_analyzer": {
        "type": "custom",
        "tokenizer": "standard",
        "filter": [
          "lowercase",
          "stemmer_filter"
        ]
      },
      "synonym_analyzer": {
        "type": "custom",
        "tokenizer": "standard",
        "filter": [
          "lowercase",
          "synonym_filter"
        ]
      }
    }
  }
}'

curl -X PUT "http://localhost:9201/codex-10-14-2024/_mapping" -H "Content-Type: application/json" -u elastic:JyzOSl9yte-f7PgXTk+v  -d '{
  "properties": {
    "title": {
      "type": "text",
      "analyzer": "autocomplete_analyzer",
      "search_analyzer": "standard"
    },
    "description": {
      "type": "text",
      "analyzer": "stemmed_analyzer",
      "search_analyzer": "standard"
    },
    "tags": {
      "type": "text",
      "analyzer": "synonym_analyzer",
      "search_analyzer": "standard"
    }
  }
}'

curl -X PUT "http://localhost:9201/codex-10-22-2024" -H "Content-Type: application/json" -u elastic:JyzOSl9yte-f7PgXTk+v -d '{
  "settings": {
    "analysis": {
      "filter": {
        "autocomplete_filter": {
          "type": "edge_ngram",
          "min_gram": 2,
          "max_gram": 20
        },
        "stemmer_filter": {
          "type": "stemmer",
          "language": "english"
        },
        "synonym_filter": {
          "type": "synonym",
          "synonyms": [
            "run, running",
            "jump, jumping",
            "walk, walking"
          ]
        }
      },
      "analyzer": {
        "autocomplete_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "autocomplete_filter"
          ]
        },
        "stemmed_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "stemmer_filter"
          ]
        },
        "synonym_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "synonym_filter"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "title": {
        "type": "text",
        "analyzer": "autocomplete_analyzer",
        "search_analyzer": "standard"
      },
      "description": {
        "type": "text",
        "analyzer": "stemmed_analyzer",
        "search_analyzer": "standard"
      },
      "tags": {
        "type": "text",
        "analyzer": "synonym_analyzer",
        "search_analyzer": "standard"
      }
    }
  }
}'

curl -X POST "http://localhost:9201/_reindex" -H "Content-Type: application/json" -u elastic:JyzOSl9yte-f7PgXTk+v -d '{
  "source": {
    "index": "codex-10-14-2024"
  },
  "dest": {
    "index": "codex-10-22-2024"
  }
}'

curl -X POST "http://localhost:9201/codex-10-14-2024/_open" -H "Content-Type: application/json" -u elastic:JyzOSl9yte-f7PgXTk+v