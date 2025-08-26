# Pub/Sub System with FastAPI, Kafka, and MongoDB

This project implements a **Pub/Sub architecture** using **FastAPI**, **Kafka**, and **MongoDB**.  
It processes the **20 Newsgroups dataset** and splits the messages into two categories:
- `interesting`
- `not_interesting`

The system consists of:
- **Publisher (FastAPI service)** → publishes messages to Kafka.
- **Two Subscribers (FastAPI services)** → consume messages from Kafka, save them to MongoDB, and provide a GET endpoint to retrieve stored messages.
- **MongoDB** → stores messages with a timestamp field.
- **Kafka & Zookeeper** → message broker infrastructure.

---

## How It Works

1. **Publisher**
   - Loads the `20 Newsgroups` dataset from `scikit-learn`.
   - Splits into two groups: `interesting` and `not_interesting`.
   - Publishes **20 random messages per group** to Kafka.

2. **Subscribers**
   - Each subscriber listens to one topic (`interesting` or `not_interesting`).
   - When a new message arrives, it:
     - Adds a `timestamp`.
     - Stores the message in MongoDB.
   - Provides a `GET /messages` endpoint to retrieve stored messages.

3. **MongoDB**
   - One database (`pubsubDB`).
   - Two collections: `interesting` and `not_interesting`.

---

## Running with Docker

Make sure you are in the project root (`pubsub-project/`):

```bash
docker-compose up --build