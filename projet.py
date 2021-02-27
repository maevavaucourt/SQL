import sqlite3 # j'importe le module sqlite3
conn = sqlite3.connect('data/imdb.db') # connection à la base de données
c = conn.cursor() # connection interface, objet cursor
#c.execute("SELECT DISTINCT (titleType) FROM title_basics;") # execution de la requete
#for row in c: # pour chaque ligne dans la base
   #print(row[0]) # renvoie ligne


with open ("requetes/req3.sql", "r") as filin: # j'ouvre la requete 1 comme un objet ( qui sera refermée automatiquement)
    requete = ""
    ligne = filin.readline() # création de la variable ligne sous laquelle il y a la méthode filin.readline()
    requete = ligne
    while ligne!= "": # Tant que ligne n'est pas vide
        ligne = filin.readline()# lit une ligne du fichier renvoyée sous chaine de caractère
        requete = requete + ligne
    print(requete) # je renvoie ligne

c.execute(requete) # execution de la requete
for row in c: # pour chaque ligne dans la base
   print(row[0]) # renvoie ligne

