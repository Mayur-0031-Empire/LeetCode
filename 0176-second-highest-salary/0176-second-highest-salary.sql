# Write your MySQL query statement below
SELECT max(salary) AS SecondhighestSalary
FROM Employee
WHERE Salary < (
    SELECT MAX(Salary) 
    FROM Employee
);