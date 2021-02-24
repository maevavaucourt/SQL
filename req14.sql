SELECT COUNT(tconst)
FROM title_basics
WHERE titleType = "movie" AND runtimeMinutes > 180;
