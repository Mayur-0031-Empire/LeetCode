# Write your MySQL query statement below
SELECT w.id 
FROM Weather w, Weather w2
WHERE DATEDIFF(w.recordDate, w2.recordDate) = 1 AND w.Temperature > w2.Temperature;