SELECT primaryName, category, job
FROM title_principals, name_basics, title_basics, title_akas
WHERE titleType = "movie" AND title = "Return of the Jedi"
AND title_akas.titleId = title_principals.tconst
AND title_principals.nconst = name_basics.nconst
AND title_basics.tconst = title_principals.tconst;