SELECT originalTitle
FROM title_basics,title_principals, name_basics
WHERE titleType = "movie"
AND name_basics.primaryName = "Olivier Nakache"
AND name_basics.nconst = title_principals.nconst
AND title_principals.tconst = title_basics.tconst;
 