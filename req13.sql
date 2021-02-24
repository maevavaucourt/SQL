SELECT originalTitle
FROM title_basics
INNER JOIN title_ratings ON title_basics.tconst = title_ratings.tconst
WHERE genres LIKE "%Animation%" AND titleType = "movie"
AND numVotes > 1000
ORDER BY averageRating DESC
LIMIT 10;