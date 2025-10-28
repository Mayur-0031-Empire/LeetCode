# Write your MySQL query statement below
SELECT 
    emp.name AS "Employee"
FROM Employee emp
JOIN Employee Manager ON emp.managerId = Manager.id
Where 
    emp.managerId IS NOT NULL AND
    emp.salary > Manager.Salary;