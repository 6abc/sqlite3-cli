-- Table Name   = members
-- Column Name  = id, last_name, last_name
BEGIN;
SELECT * FROM members WHERE last_name LIKE '%dave%';
COMMIT;