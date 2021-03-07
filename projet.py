import sqlite3 # j'importe le module sqlite3


#DicoReq = {}
#with open ("requetes/alire.md") as filin:


requete = ""

#------------------------------------------
#Bloc de fonctions
#------------------------------------------

def lire(NomRequete):
    """
    Fonction qui lit la requete demandée.
    """

    fichier = (NomRequete) + ".sql"
    with open ("requetes/" + fichier, "r") as filin: # j'ouvre la requete comme un objet ( qui sera refermée automatiquement)
        requetelu = ""
        ligne = filin.readline() # création de la variable ligne sous laquelle il y a la méthode filin.readline()
        requetelu = ligne
        while ligne!= "": # Tant que ligne n'est pas vide
            ligne = filin.readline()# lit une ligne du fichier renvoyée sous chaine de caractère
            requetelu = requetelu + ligne
        return requetelu
        #print(requete) # je renvoie ligne

def executer(ReqDB):

    c.execute(ReqDB) # execution de la requete
    for row in c: # pour chaque ligne dans la base
        print(row[0]) # renvoie lignes

def afficher_table(table, debut = None, fin = None):
    for row in table (debut,fin):
        print(row)



#def projection_table(table,NumColonnes):

#    for row in table:
#        print (row[NumColonnes]))


#------------------------------------------
#Fin bloc fonctions
#------------------------------------------

#Connexion BDD
conn = sqlite3.connect('data/imdb.db') # connection à la base de données
c = conn.cursor() # connection interface, objet cursor

#Lit une requete
requete=lire("req1")
#print(requete)

#execution requete
reslult = executer(requete)

afficher_table(name_titles, 0, 10)

#Fin de connexion BDD
conn.close()
