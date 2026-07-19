-- Lists all records of second_table where name is not empty, ordered by score descending
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
