CREATE Table IF NOT EXISTS restaurant (
    RESTAURANT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    RESTAURANT_NAME TEXT,
    NEIGHBOURHOOD TEXT,
    CUISINE TEXT,
    REVIEW REAL,
    PRICE TEXT,
    HEALTH TEXT
);


INSERT INTO restaurant(RESTAURANT_NAME, NEIGHBOURHOOD, CUISINE, REVIEW, PRICE, HEALTH) VALUES
    ("Layar", "Jakarta", "Seafood", 4.4, "$$$$", "A"),
    ("RM Surya", "Jakarta", "Indonesian", 4.5, "$$$", "A"),
    ("Ahjumma Kicthen", "Surabaya", "Korean", 3.5, "$$", "A"),
    ("Pizza e Birra", "Surabaya", "Pizza", 4, "$$$", "B"),
    ("Spice Affair", "Bandung", "Indian", 3.9, "$", "A"),
    ("Prabhu Curry House", "Bandung", "Indian", 4.6, "$$$", "B"),
    ("Moi Garden Hakka", "Surabaya", "Chinese", 3.0, "$$", "B"),
    ("L'Osteria Pizza e CUcina", "Ubud", "Italian", 4.9, "$$$$", "B"),
    ("Paparons Pizza", "Surabaya", "Pizza", 3.8, "$$$", "A"),
    ("Warung Italia", "Ubud", "Italian", 3.8, "$$$", "A");

--Select all records from the restaurant table--
SELECT * FROM restaurant;

--Select distnict neighbourhoods from the restaurant table--
Select DISTINCT NEIGHBOURHOOD FROM restaurant;

--select distinct cuisines from the restaurant table
SELECT DISTINCT CUISINE FROM restaurant;

--Select all records with chinese cuisine--
SELECT *FROM restaurant WHERE CUISINE = "Chinese";

--Select all records with a review rating of 4 or higher
SELECT * FROM restaurant WHERE REVIEW >= 4;

--Select all records with italian cuisine and $$$ price
SELECT * FROM restaurant WHERE CUISINE = "Italian" AND PRICE = "$$$";

--select all records where th RESTAURANT_NAME contains "PIzza";
SELECT * FROM restaurant WHERE RESTAURANT_NAME LIKE "%Pizza%";

--select all records where the neighbourhood is Surabaya, Bandung or Ubud
SELECT * FROM restaurant
WHERE NEIGHBOURHOOD IN ("Surabaya", "Bandung", "Ubud");

--select the first 3 records with review at least 4 ordered by review rating in ascending order
SELECT * FROM restaurant WHERE REVIRE LIKE "4%" ORDER BY REVIEW LIMIT 3;

--Select the top 4 records ordered by review rating in descending order
SELECT * FROM restaurant ORDER BY REVIEW DESC LIMIT 4;
