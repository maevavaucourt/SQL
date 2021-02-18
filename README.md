

3.
 SELECT startYear
FROM title_basics
WHERE primaryTitle = "The Godfather" AND  titleType = "movie";
--> 1972

4. 
SELECT MIN ( startYear )
FROM title_basics
WHERE primaryTitle = "Superman" AND  titleType = "movie";
--> 
