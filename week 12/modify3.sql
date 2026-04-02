-- Modify #3

-- This query shows all customers in the database
SELECT * FROM Customers;

-- This query shows products that cost more than $25
SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice > 25;

-- This query sorts employees by last name
SELECT FirstName, LastName
FROM Employees
ORDER BY LastName;

-- This query joins Products and Categories to show product names with their category
SELECT p.ProductName, c.CategoryName
FROM Products p
JOIN Categories c
ON p.CategoryID = c.CategoryID;

-- This query counts how many customers are in each country
SELECT Country, COUNT(*) AS TotalCustomers
FROM Customers
GROUP BY Country;
