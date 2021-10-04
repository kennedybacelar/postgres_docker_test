#!/bin/bash
set -e

echo "******PostgreSQL initialisation --- Rolando******"

psql -v ON_ERROR_STOP=1 --username $POSTGRES_USER --dbname $POSTGRES_DB <<-EOSQL

  CREATE TABLE IF NOT EXISTS users(
    user_id INT PRIMARY KEY NOT NULL,
    age         VARCHAR(5),
    country     VARCHAR(2)
  );

  CREATE TABLE IF NOT EXISTS user_interaction(
    event_id VARCHAR(36) PRIMARY KEY NOT NULL,
    user_id  INT REFERENCES users (user_id),
    event_type VARCHAR(5),
    event_time TIMESTAMP
  );

EOSQL
