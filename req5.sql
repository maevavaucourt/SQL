#05.Quel est le titre original du film 'Les dents de la mer' ? 
SELECT originalTitle
FROM title_basics
INNER JOIN title_akas ON title_basics.tconst = title_akas.titleId
WHERE title = "Les dents de la mer"
AND titleType = "movie";