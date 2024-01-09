-- Table Name   = members
-- Column Name  = id, first_name, last_name
BEGIN;
CREATE TABLE IF NOT EXISTS members (id INTEGER PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NULL);
INSERT INTO members VALUES (1, "Steve", "Coplan");
INSERT INTO members VALUES (2, "Dave", "Colan");
INSERT INTO members VALUES (3, "Mike", "Olan");
INSERT INTO members VALUES (4, "Eps", "Plan");
INSERT INTO members VALUES (5, "Bog", "Lan");
INSERT INTO members VALUES (6, "Dog", "Lan");
COMMIT;