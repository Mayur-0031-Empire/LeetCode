# Write your MySQL query statement below
SELECT
    c.name AS "Customers"
FROM 
    Customers c
WHERE 
    c.id NOT IN (
        SELECT cus.id FROM Customers cus
        INNER JOIN Orders o ON cus.id = o.customerId
    );
