# Write your MySQL query statement below
SELECT P.product_id, IF(COUNT(U.purchase_date) > 0, ROUND(SUM(P.price * U.units) / SUM(U.units), 2), 0.00) AS average_price
FROM Prices AS P
LEFT JOIN UnitsSold AS U
    ON P.product_id = U.product_id 
    AND P.start_date <= U.purchase_date
    AND P.end_date >= U.purchase_date
GROUP BY P.product_id