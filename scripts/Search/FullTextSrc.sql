-- Table Name   = members
-- Column Name  = id, first_name, last_name
BEGIN;
SELECT * FROM members WHERE first_name = 'Dave';
COMMIT;