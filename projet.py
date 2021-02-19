import sqlite3
conn = sqlite3.connect('data/imdb.db')
c = conn.cursor()
c.execute("select * from name_basics limit 10")
for row in c:
    print(row)
conn.close()

with open ("requetes/req1.sql", "r") as filin:
    ligne = filin.readline()
    while ligne!= "":
        print(ligne)
        ligne = filin.readline()








