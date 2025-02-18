SELECT m.title, COUNT(r.movID) AS play_count
FROM movies m
JOIN record r ON m.movID = r.movID
JOIN friend f ON r.userid = f.userid2
WHERE f.userid1 = %s
GROUP BY m.title
ORDER BY play_count DESC
LIMIT 20;

