# Write your MySQL query statement below
SELECT S.user_id, IF(COUNT(action) > 0, ROUND(SUM(IF(C.action = 'Confirmed', 1, 0))/COUNT(action), 2), 0.00) AS confirmation_rate
FROM Signups AS S
LEFT JOIN Confirmations AS C
    ON S.user_id = C.user_id
GROUP BY S.user_id