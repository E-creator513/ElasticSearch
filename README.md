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
