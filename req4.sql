#04. En quelle annee est sortie le premier film Superman ? 
SELECT MIN ( startYear )
FROM title_basics
WHERE primaryTitle = "Superman" AND  titleType = "movie";