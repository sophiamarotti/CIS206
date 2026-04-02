-- Modify #1

-- Show all customers
SELECT * FROM Customers;

-- Show all employees
SELECT * FROM Employees;

-- Show all products
SELECT * FROM Products;

-- Show products over $20
SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice > 20;

-- Show customers from Germany
SELECT CustomerID, CompanyName, Country
FROM Customers
WHERE Country = 'Germany';
