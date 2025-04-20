# Elastic Stack

A Complete Setup Guide for Elasticsearch, Logstash, and Kibana with Docker Compose

## Prerequisites

- Docker & Docker Compose installed on your machine
- Minimum 4GB of RAM


## Deployment

1. **Clone the repository:**

    ```bash
    git clone https://github.com/ncsonn/elastic-stack.git
    cd elastic-stack
    ```


2. **Initialize Elasticsearch:**

    _Step 1: Create a Setup Node_

    ```bash
    # Start and enter the setup container
    docker-compose -f docker-compose-init.yml up -d

    # Copy instances.yml into container
    docker cp ./config/instances.yml elastic-setup:/usr/share/elasticsearch/config/instances.yml

    # Navigate into the setup container
    docker exec -it elastic-setup bash
    ```

    _Step 2: Start and Enter the Setup Container_

    ```bash
    # Generate the CA certificate
    bin/elasticsearch-certutil ca --silent --pem -out config/certs/ca.zip
    unzip config/certs/ca.zip -d config/certs


    # Generate node certificates using the CA
    bin/elasticsearch-certutil cert --silent --pem -out config/certs/certs.zip \
    --in config/instances.yml \
    --ca-cert config/certs/ca/ca.crt \
    --ca-key config/certs/ca/ca.key
    unzip config/certs/certs.zip -d config/certs


    # Reset the Kibana system user password
    bin/elasticsearch-reset-password -u kibana_system
    ```

    _Step 3: Copy the Generated Certificates_

    ```bash
    # Exit & copy the generated certificates to your host machine
    docker cp elastic-setup:/usr/share/elasticsearch/config/certs ./config/
    ```

    _Step 4: Clean Up_

    ```bash
    # Stop and remove the setup container
    docker-compose -f docker-compose-init.yml down
    ```


3. **Start the services:**

    ```bash
    docker-compose up -d
    ```


4. **Send test logs:**

    ```bash
    # Install libraries
    pip install python-logstash

    # Run example.py to send test logs to Logstash
    python example.py
    ```


5. **Verify log ingestion:**

    If everything is configured correctly, after sending logs to Logstash, you should see a new index created in Elasticsearch.

    1. Open Kibana in your browser: https://localhost:5601

    2. Navigate to Stack Management > Index Management. Look for an index named something like: example-logs


## Stopping the Services

To stop the services, run:

```sh
docker-compose down
```


## Cleaning Up

To remove all containers, networks, and volumes, run:

```sh
docker-compose down --volumes --remove-orphans
```