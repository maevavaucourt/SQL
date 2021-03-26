#14.Combien de films durent plus de 3 heures ?
SELECT COUNT(tconst)
FROM title_basics
WHERE titleType = "movie" AND runtimeMinutes > 180;
