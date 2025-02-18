SELECT m.title
FROM movies m
JOIN releasing r ON m.movID = r.movID
WHERE EXTRACT(MONTH FROM r.releasedate) = %s
AND EXTRACT(YEAR FROM r.releasedate) = %s
ORDER BY r.releasedate DESC
LIMIT 5;

