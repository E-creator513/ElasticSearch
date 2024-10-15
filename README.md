# ElasticSearch Project

Hello! This project initiates an introduction to the use of ES Data-Nodes.I would recommend you clone the repository on your local machine and give it a try,I am very open to suggestions and corrections,its still an ongoing work.Enjoy!

## Cloning

To clone the project, run the following command:

```bash
$ git clone https://github.com/E-creator513/ElasticSearch.git
```
##  ElasticSearch Activation

You can navigate to the Dockerfiles to start the single-node Elasticsearch cluster

```bash
$ docker-compose up --build
```

I have already added the mock data in the data-node but just in case you have new data(with arrays of objects),first run the file convert.py and name it mocks_es_format.json
After the docker-compose is up you should check the health status in the terminal and see the result in a browser extn

 ```bash
{
  "name" : "d3b9379848f9",
  "cluster_name" : "docker-cluster",
  "cluster_uuid" : "iokHUTmPTtOJyP5xuGw8fA",
  "version" : {
    "number" : "8.0.0",
    "build_flavor" : "default",
    "build_type" : "docker",
    "build_hash" : "1b6a7ece17463df5ff54a3e1302d825889aa1161",
    "build_date" : "2022-02-03T16:47:57.507843096Z",
    "build_snapshot" : false,
    "lucene_version" : "9.0.0",
    "minimum_wire_compatibility_version" : "7.17.0",
    "minimum_index_compatibility_version" : "7.0.0"
  },
  "tagline" : "You Know, for Search"
}
```
After you are certain the network is health you should start the flask app framework 

 ```bash
python app.py
```
This app will automatically connect to the ES Single-cluster using the credentials aforementioned already inside 

## Interaction
There are two ways to interact with this database ,through the index on address http://127.0.0.1:5000 with a landing page like this 
![image](https://github.com/user-attachments/assets/0b5f0dfe-5a08-4b59-b492-b6e05e90aca2)
## Terminal
Through the git-bash terminal with these commands 
### Searching 

for example the word Editor.js
```bash
curl -X GET "http://localhost:5000/search?querystring=Editor.js" -H "Content-Type: application/json"
```
you should be getting the result like 

```bash
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1856  100  1856    0     0   6642      0 --:--:-- --:--:-- --:--:--  6652{
  "documents": [
    {
      "fieldContent": "You can destroy an Editor.js instance by calling the `destroy` method.",
      "fieldName": "content",
      "id": "29"
    },
    {
      "fieldContent": "You can destroy an Editor.js instance by calling the `destroy` method.",
      "fieldName": "content",
      "id": "hmtni5IB-CXDxQLHAUBM"
    },
    {
      "fieldContent": "You can destroy an Editor.js instance by calling the `destroy` method.",
      "fieldName": "content",
      "id": "rmtxi5IB-CXDxQLHgEBl"
    },
    {
      "fieldContent": "You can destroy an Editor.js instance by calling the `destroy` method.",
      "fieldName": "content",
      "id": "1Wtzi5IB-CXDxQLH6EDn"
    },
    {
      "fieldContent": "In this guide, we will learn how to interact with the Editor.js API.",
      "fieldName": "content",
      "id": "37"
    },
    {
      "fieldContent": "In this guide, we will learn how to interact with the Editor.js API.",
      "fieldName": "content",
      "id": "jmtni5IB-CXDxQLHAkD1"
    },
    {
      "fieldContent": "In this guide, we will learn how to interact with the Editor.js API.",
      "fieldName": "content",
      "id": "tmtxi5IB-CXDxQLHgkCw"
    },
    {
      "fieldContent": "In this guide, we will learn how to interact with the Editor.js API.",
      "fieldName": "content",
      "id": "3Wtzi5IB-CXDxQLH6kBA"
    },
    {
      "fieldContent": "Since version 2.18, Editor.js provides an API for internationalization (i18n) that allows localizing all UI texts of the editor's core and plugins.",
      "fieldName": "content",
      "id": "30"
    },
    {
      "fieldContent": "Since version 2.18, Editor.js provides an API for internationalization (i18n) that allows localizing all UI texts of the editor's core and plugins.",
      "fieldName": "content",
      "id": "h2tni5IB-CXDxQLHAUB1"
    }
  ]
}
```
### Patch
To update an existing document using its Id, use the PATCH method.
 
```bash
$ curl -X PATCH http://localhost:5000/document -H "Content-Type: application/json" -d '{
    "documentId": "1",
    "document": {
        "title": "Updated Title",
        "content": "Updated content for the document."
    }
}'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   259  100   120  100   139    439    508 --:--:-- --:--:-- --:--:--   945{
  "document": {
    "content": "Updated content for the document.",
    "id": "1",
    "title": "Updated Title"
  }
}
```
Avoid randomly using an unknown id ,i have made sure ES automatically generates them also

### Creating a document also
```bash
curl -X POST "http://localhost:5000/document" -H "Content-Type: application/json" -d @data.json
```

