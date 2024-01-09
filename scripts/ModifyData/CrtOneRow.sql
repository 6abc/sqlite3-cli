-- Table Name   = members
-- Column Name  = id, first_name, last_name
BEGIN;
CREATE TABLE IF NOT EXISTS members (id INTEGER PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NULL);
INSERT INTO members VALUES (1, "Steve", "Coplan");
COMMIT;