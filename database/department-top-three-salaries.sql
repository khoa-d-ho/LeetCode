# Write your MySQL query statement below
SELECT Department, Employee, Salary
FROM (
    SELECT 
    D.name AS Department, E.name AS Employee, E.salary AS Salary, DENSE_RANK() OVER (PARTITION BY E.departmentID ORDER BY E.salary DESC) AS r
FROM Employee E
INNER JOIN Department D
    ON E.departmentId = D.id
) AS sub1
WHERE r IN (1, 2, 3)

