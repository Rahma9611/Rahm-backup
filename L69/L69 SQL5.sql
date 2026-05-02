CREATE TABLE IF  NOT EXISTS Grocery_Product (
    PRODUCT_ID TEXT PRIMARY KEY,
    PRODUCT_NAME TEXT,
    SUPPLIER_ID TEXT,
    CATEGORY_ID TEXT,
    UNIT TEXT,
    PRICE REAL
);

INSERT INTO Grocery_Product (PRODUCT_ID, PRODUCT_NAME, SUPPLIER_ID, CATEGORY_ID, UNIT, PRICE) VALUES
("P001", "Tea", "S001", "C01", "10 boxes * 20 bags", 35),
("P002", "Kethcup", "S001", "C01", "24 - 12 oz bottles", 25),
("P003", "Maple Syrup", "S001", "C02", "12 - 550 ml bottles", 17),
("P004", "Cucumber pickle", "S002", "C02", "48 - 6 oz jars", 23),
("P005", "Tisane", "S002", "C02", "36 boxes", 25.7);

-- query to count the number of Grocery_Products
SELECT COUNT(PRODUCT_ID) AS Product_Count FROM Grocery_Product;

-- query to find the average price of  Grocery_Products
SELECT AVG(PRICE) AS Average_Price FROM Grocery_Product;

-- query to find the total price of  Grocery_Products
SELECT SUM(PRICE) AS Total_Price FROM Grocery_Product;