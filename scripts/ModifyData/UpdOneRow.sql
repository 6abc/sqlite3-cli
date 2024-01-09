-- Table Name   = members
-- Column Name  = id, first_name, last_name
BEGIN;
UPDATE members SET last_name = "Coplan" WHERE id = 1;
COMMIT;