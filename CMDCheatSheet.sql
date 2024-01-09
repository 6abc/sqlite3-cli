-- SQLite Cheat Sheet https://www.sqlitetutorial.net/sqlite-cheat-sheet/

-- !Managing databases
-- Attach another database to the current database connection:
ATTACH DATABASE old_sql.db AS new_sql.db;
-- Optimize the database:
VACUUM

-- !Managing Tables---
-- Create a new table:
CREATE TABLE IF NOT EXISTS members (id INTEGER PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NULL);
-- Rename a table:
ALTER TABLE old_table RENAME TO new_table;
-- Add a new column to a table:
ALTER TABLE table ADD COLUMN new_column;
-- Drop an existing column in a table:
ALTER TABLE table DROP COLUMN column_name;
-- Drop a table and its data:
DROP TABLE IF EXISTS table_name;

-- !Managing indexes---
-- Creating an index:

-- Delete an index:
ATTACH DATABASE file_name AS database_name;
-- Create an expression index:
CREATE INDEX index_name ON table_name(expression);

-- !Querying Data---
-- Query all data from a table:
SELECT * FROM table_name;

-- !Changing Data---
-- CRUD
-- Insert a row into a table:
INSERT INTO table_name(column1,column2,...) VALUES(value_1,value_2,...);
-- Insert multiple rows into a table in a single statement:
INSERT INTO table_name(column1,column2,...) VALUES(value_1,value_2,...),(value_1,value_2,...),(value_1,value_2,...);

-- !Search---
-- Search using LIKE operator:
SELECT * FROM table WHERE column LIKE '%value%';
-- Search using full-text search:
SELECT * FROM table WHERE table MATCH 'search_query';