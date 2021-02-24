SELECT originalTitle
FROM title_basics
INNER JOIN title_akas ON title_basics.tconst = title_akas.titleId
WHERE title = "Les dents de la mer"
AND titleType = "movie";
