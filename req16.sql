#16.Quel est le film le plus long ? 
SELECT originalTitle
FROM title_basics
WHERE titleType = "movie"
ORDER BY runtimeMinutes DESC
LIMIT 1;