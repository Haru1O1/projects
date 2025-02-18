SELECT DISTINCT m.title
FROM movies m
JOIN record r ON m.movID = r.movID
JOIN movieshasgenre gm ON m.movid = gm.movid
JOIN acts_in a ON m.movid = a.movid
WHERE r.timestamp >= NOW() - INTERVAL '90 days' AND (gm.genreid = %s OR a.id = %s)
GROUP BY m.title
ORDER BY m.title DESC
LIMIT 10;

