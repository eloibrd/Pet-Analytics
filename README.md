# Pet Analytics

## Prerequisites

- [x] Docker
- [x] Docker compose
- [x] Python 3
- [x] Poetry (Python dependencies and venv manager)

## Install

```
# Install deps
poetry install

# Create .env
cp .env.example .env
```

## Run

```
# Start influx and grafana containers
docker compose up

# Bash script to run fastapi app localy
./run.sh
```
