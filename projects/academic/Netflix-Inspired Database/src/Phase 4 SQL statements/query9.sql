SELECT c.name AS actor_name, a.id AS actor_id
FROM movies m
JOIN record r ON m.movID = r.movID
JOIN acts_in a ON m.movid = a.movid
JOIN contributors c ON a.id = c.id
WHERE r.userid = %s
GROUP BY actor_name, actor_id
ORDER BY COUNT(r.movID) DESC
LIMIT 1;

