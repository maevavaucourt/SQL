#09.Qui a ecrit le scenario du film Taxi sorti en 1998 ?
SELECT primaryName
FROM name_basics, title_principals, title_basics
WHERE titleType = "movie" AND startYear = 1998 AND originalTitle = "Taxi"
AND title_basics.tconst = title_principals.tconst
AND title_principals.nconst = name_basics.nconst
AND title_principals.job = "scenario";