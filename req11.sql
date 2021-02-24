SELECT originalTitle
FROM title_basics
INNER JOIN title_ratings ON title_basics.tconst = title_ratings.tconst
WHERE averageRating > 9 AND numVotes > 10000 AND titleType = "movie";