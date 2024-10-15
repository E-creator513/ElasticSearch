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

##Interaction

