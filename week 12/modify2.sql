-- Modify #2

-- INSERT a new customer
INSERT INTO Customers (
    CustomerID, CompanyName, ContactName, Country
) VALUES (
    'NEW01', 'Sophia Co', 'Sophia Marotti', 'USA'
);

-- UPDATE that customer
UPDATE Customers
SET City = 'Chicago'
WHERE CustomerID = 'NEW01';

-- DELETE that customer
DELETE FROM Customers
WHERE CustomerID = 'NEW01';
