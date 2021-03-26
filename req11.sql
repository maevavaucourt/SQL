#11.Quels sont les titres des films notes plus de 9 sur 10 avec plus de 10 000 votes ?
SELECT originalTitle
FROM title_basics
INNER JOIN title_ratings ON title_basics.tconst = title_ratings.tconst
WHERE averageRating > 9 AND numVotes > 10000 AND titleType = "movie";