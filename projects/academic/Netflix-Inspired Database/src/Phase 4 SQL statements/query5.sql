SELECT m.title, COUNT(r.movID) AS play_count
FROM movies m
JOIN record r ON m.movID = r.movID
WHERE r.timestamp >= NOW() - INTERVAL '90 days'
GROUP BY m.title
ORDER BY play_count DESC
LIMIT 20;

