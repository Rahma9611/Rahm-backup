CREATE TABLE IF NOT EXISTS students (
    ROLL_NO TEXT PRIMARY KEY,
    SNAME TEXT NOT NULL,
    SADDRESS TEXT,
    PHONE TEXT,
    AGE INTEGER
);

--Insert sample data into the student table
INSERT INTO STUDENTS (ROLL_NO, SNAME, SADDRESS, PHONE, AGE) VALUES
('1', 'Andrew', 'Jakarta', '+62-134573248', 17),
('2', 'Jack', 'Mesaieed', '974-5522768', 18),
('3', 'Ashley', 'Doha', '974-5559012', 20),
('4', 'Randy', 'Al-Rayyan', '974-5513456', 18),
('5', 'Jessica', 'Al-Khor', '974-5567890', 20),
('6', 'Abdul', 'Lusail', '974-5567890', 18);

--select all records from the salesman table to verify insertion (if required)
SELECT * FROM Salesman;

-- select all records from the students table to verify insertion
SELECT * FROM students;

-- query students who are 18 years old and live in Al-Rayyan
SELECT * FROM students WHERE AGE = 18 AND SADDRESS = 'Al-Rayyan';   

-- query students who are 18 years old and named Andrew
SELECT * FROM students WHERE AGE = 18 AND SNAME = 'Andrew';

-- query students named Jack or Ashley
SELECT * FROM students WHERE SNAME = 'Jack' OR SNAME = 'Ashley';

-- query students named jessica or live in Lusail
SELECT * FROM students WHERE SNAME = 'Jessica' OR SADDRESS = 'Lusail';

-- query students aged 18 and named Randy or abdul
SELECT * FROM students WHERE AGE = 18 AND (SNAME = 'Randy' OR SNAME = 'Abdul'); 