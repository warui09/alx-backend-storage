-- creates an index on the table names
DROP INDEX IF EXISTS idx_name_first ON names;

CREATE INDEX idx_name_first
ON names (name LIKE 'a%';
