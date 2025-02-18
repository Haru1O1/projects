SELECT g.genretype, gm.genreid
FROM movies m
JOIN movieshasgenre gm ON m.movid = gm.movID
JOIN record r ON m.movID = r.movID
JOIN genre g ON gm.genreid = g.genreid
WHERE r.userid = %s
GROUP BY g.genretype, gm.genreid
ORDER BY COUNT(gm.genreid) DESC
LIMIT 1;

