# Write your MySQL query statement below
SELECT E.name
FROM (SELECT managerId
FROM Employee
GROUP BY managerId
HAVING COUNT(id) >= 5) AS sub1
INNER JOIN Employee AS E
    ON sub1.managerId = E.id