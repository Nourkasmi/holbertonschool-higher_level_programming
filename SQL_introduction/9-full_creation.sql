-- Script to create the table second_table and insert multiple rows

CREATE TABLE IF NOT EXISTS second_table (
    name VARCHAR(256)?
    id INT,
    score INT,
)

INSERT INTO second_table (name, id, score) VALUES
     ('John', 1, 10),
     ('Alex', 2, 3),
     ('Bob', 3, 14),
     ('George', 4, 8);
