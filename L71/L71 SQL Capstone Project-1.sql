CREATE TABLE IF NOT EXISTS Salesperson (
    Salesperson_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    Comission REAL
);

INSERT INTO Salesperson (Salesperson_id, name, city, comission) VALUES
    ("7001", "Jessica Wong", "Berlin", 0.18),
    ("7002", "James White", "Paris", 0.17),
    ("7003", "Andrew Smith", "London", 0.17),
    ("7004", "Alex McGrager", "New York", 0.18),
    ("7005", "Paul Adam", "Copenhagen", 0.17),
    ("7006", "Tristan Alexander", "Moscow", 0.11);

CREATE TABLE IF NOT EXISTS Cust (
    customer_id TEXT, 
    cust_name TEXT PRIMARY KEY,
    city TEXT,
    grade INTEGER,
    Salesperson_id TEXT,
    FOREIGN KEY (Salesperson_id) REFERENCES Salesperson(Salesperson_id)
);

INSERT INTO Cust (customer_id, cust_name, city, grade, Salesperson_id) VALUES
    ("C1001" "Jay Idzes", "New York", 100, "7004"),
    ("C1002" "Justin Hubner", "London", 300, "7003"),
    ("C1003" "Sandy Walsh", "Moscow", 200, "7006"),
    ("C1004" "Garaga", "Paris", NULL, "7002"),
    ("C1005" "Zoe Saldana", "California", 200, "7004"),
    ("C1006" "Jowel Toyyib", "London", NULL, "7003"),
    ("C1007" "Bradd Pitt", "Copenhagen", 100, "7005"),
    ("C1008" "Andrew Smith", "London", 100, "7003"),
    ("C1009" "Ragnar Oeratmangoe", "Berlin", 100, "7001");

--create the orders table if it does not exist
CREATE TABLE IF NOT EXISTS MyOrders (
    ord_no TEXT PRIMARY KEY,
    purch_amt REAL,
    ord_date TEXT,
    customer_id TEXT,
    Salesperson_id TEXT,
    FOREIGN KEY (customer_id) REFERENCES Cust(customer_id)
    FOREIGN KEY (salesperson_id) REFERENCES Salesperson(Salesperon_id)
);

--Insert sample data into the Orders table
INSERT INTO MyOrders (ord_no, purch_amt, ord_date, customer_id, Salesperson_id) VALUES
    ("P30001", 175.5, "2024-10-05", "C1005", "7002"),
    ("P30002", 375.65, "2024-09-10", "C1001", "7001"),
    ("P30003", 55.26, "2024-10-10", "C1002", "7003"),
    ("P30004", 210.5, "2024-08-10", "C1009", "7007"),
    ("P30005", 849.5, "2024-09-10", "C1005", "7005"),
    ("P30006", 2700.6, "2024-07-10", "C1007", "7006");



-- Matching customers and salesman by city
SELECT Cust.cust_name, Salesperson.name, Salesperson.city
FROM Cust
JOIN Salesperson ON Cust.city = Salesperson.city;

-- Linking customers to their salesmen
SELECT Cust.cust_name, Salesperson.name
FROM Cust
JOIN Salesperson ON Cust.Salesperson_id = Salesperson.Salesperson_id;

-- Fetching orders where customer's city does not match Salesperon's city
SELECT MyOrders.ord_no, Cust.cust_name, MyOrders.customer_id, MyOrders.Salesperson_id
FROM MyOrders
JOIN Cust ON MyOrders.customer_id = Cust.customer_id
JOIN Salesperson ON MyOrders.Salesperson_id = Salesperson_id
WHERE Cust.city <> Salesperson.city;

--fetching all orders with customer names
SELECT MyOrders.ord_no, Cust.cust_name
FROM MyOrders
JOIN Cust ON MyOrders.customer_id = Cust.customer_id;