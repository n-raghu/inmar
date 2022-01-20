# BAKERY STOCK APIs
#### Task Challenge from INMAR

## Salient Features developed
- `FastAPI` framework to host all the APIs requested
- Created wrappers for DB operations which can be imported and used by any future APIs or services
- Integrated the in-built `Swagger/OAS3` to run/test the APIs
- DB Schema changes are versioned using `alembic` which helps user to apply and revert the changes as done using git
- Services are deployed using `Docker` containers and a compose file is available in the orchestration folder
- `Ingestion tool` to dump CSV data to tables by simple mappings
- Implemented Pagination, total pages and row count in the response headers which helps users to know the size of data
- Every GET method of API has query param `page` with default value 1 which helps to retrieve data of specific page
- Integrated `logging` module which can be extended to log events to file
- Error mechanism is in place to record errors while processing requests


## How to start
- Navigate to `orchestration` folder
- Start the services using below command which creates 3 containers in the backend. **First container hosts the service/API, second container hosts the PostgreSQL flavor of RDBMS engine and the third container for ingestion job**
> docker-compose -f compose-inmar.yml up -d
- Hit the below URI in browser to start the OAS3 page and to play with the APIs
> <hostip>:39001/bakerystock
- Container created for ingestion job will be running idle, ingestion job can be triggered inside the container whenever new data exists.
- Running ingestion job in every cycle will create duplicate data, will need to work on archiving the ingested CSV files before running job as cycles.