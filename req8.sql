#08.Quel est le film ayant recueilli le plus de votes ?
SELECT originalTitle
FROM title_basics
INNER JOIN title_ratings ON title_basics.tconst = title_ratings.tconst
WHERE titleType = "movie" 
ORDER BY numVotes DESC
LIMIT 1;
