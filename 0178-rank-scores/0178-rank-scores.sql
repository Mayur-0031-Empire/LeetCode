# Write your MySQL query statement below
SELECT Score, DENSE_RANK() over(order by score desc )  AS rank
FROM Scores
;