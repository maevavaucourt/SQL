SELECT originalTitle, primaryName
FROM name_basics, title_basics, title_directors, title_ratings
WHERE titleType = "movie"
AND title_ratings.tconst = title_basics.tconst
AND title_basics.tconst = title_directors.tconst
AND name_basics.nconst = directors
ORDER BY averageRating DESC
LIMIT 5;
