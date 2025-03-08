-- Script to create the table unique_id with constraints

CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL DEFAULT 1, UNIQUE,
    name VARCHAR(256)
);
