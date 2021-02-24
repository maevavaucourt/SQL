SELECT originalTitle, primaryName
FROM title_principals, name_basics, title_basics
WHERE titleType = "movie" AND characters LIKE "%James Bond%" 
AND title_principals.nconst = name_basics.nconst
AND title_principals.tconst = title_basics.tconst;
