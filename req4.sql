#04. En quelle année est sortie le film The Godfather ? 
SELECT startYear
FROM title_basics
WHERE primaryTitle = "The Godfather" AND  titleType = "movie";
