# ELK Stack Docker Setup

ELK (Elasticsearch, Logstash, Kibana) stack using Docker Compose for log aggregation and analysis.

## Prerequisites

Before running this setup, ensure you have the following installed:

- **Docker** (latest version recommended) - [Installation Guide](https://docs.docker.com/get-docker/)
- **Docker Compose** - [Installation Guide](https://docs.docker.com/compose/install/)
- Minimum **4GB RAM** available for containers


## Setup Instructions

### 1. Setup Instructions
Clone the Repository
```bash
git clone https://github.com/your-username/elk-stack.git
cd elk-stack
```
Start the containers:
```bash
docker-compose up -d
```
Stop and remove containers
```bash
docker-compose down --rmi all
```

### 2. Verify Installation
Confirm that Elasticsearch is running:
```bash
curl -X GET "http://localhost:9200"
```
Verify Logstash logs:
```bash
docker-compose logs logstash
```


## License
This project is licensed under the MIT License.


