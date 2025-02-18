SELECT m.title, r.userrating
FROM movies m
JOIN rating r ON m.movID = r.movID
WHERE r.userid = %s
ORDER BY r.userrating DESC
LIMIT 10;
