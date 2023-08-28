-- this is a script to create an index
CREATE INDEX idx_name_first_score ON names(name(1), score)
