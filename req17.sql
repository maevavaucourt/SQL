#17.Quels sont les 5 films les plus longs ?
SELECT originalTitle
FROM title_basics
WHERE titleType = "movie"
ORDER BY runtimeMinutes DESC
LIMIT 5;