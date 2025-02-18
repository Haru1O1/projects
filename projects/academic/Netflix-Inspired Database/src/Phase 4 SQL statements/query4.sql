SELECT m.title, COUNT(r.movid) AS views
FROM movies m
JOIN record r ON m.movID = r.movID
WHERE r.userid = %s
GROUP BY m.title
ORDER BY views DESC
LIMIT 10;
