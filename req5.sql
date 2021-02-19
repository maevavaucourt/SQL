#05 Quel est le titre original du film 'Les dents de la mer' ? 
SELECT title_basics.originalTitle
FROM title_basics, title_akas
WHERE title_akas.title = 'Les dents de la mer'
AND titleType = 'movie'
AND title_akas.titleId = title_basics.tconst;
