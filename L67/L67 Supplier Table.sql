-- creating table
CREATE TABLE supplier (
    SupNum TEXT PRIMARY KEY,
    Supname TEXT,
    SupStatus INTEGER,
    SupCity REAL
);

-- inserting data
INSERT INTO supplier(SupNum, SupName, SupStatus, SupCity) VALUES
("S01", "Jonathan", 20, "Jakarta"),
("S02", "Andrew", 10, "Surabaya"),
("S03", "Jessia", 15, "New York"),
("S04", "Jack", 30, "Lagos"),
("S05", "Amber", 10, "London");

-- displaying all the data
SELECT * from supplier; 

