#12.Quelles sont les 5 comedies romantiques les mieux notees ? 
SELECT originalTitle
FROM title_basics
INNER JOIN title_ratings ON title_basics.tconst = title_ratings.tconst
WHERE genres LIKE "%Romance%" AND genres LIKE "%Comedy%"
ORDER BY averageRating DESC
LIMIT 5;