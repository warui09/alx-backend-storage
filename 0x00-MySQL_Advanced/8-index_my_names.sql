-- creates an index on the table names
ALTER TABLE names
ADD first_letter CHAR(1);

UPDATE names
SET first_letter = LEFT(name, 1);

CREATE INDEX idx_name_first
ON names (first_letter);
