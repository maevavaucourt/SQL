﻿import sqlite3 # j'importe le module sqlite3
import pprint

requete = ""
dico = {}

#with open ("requetes/alire.md") as filin:
#------------------------------------------
#Bloc de fonctions
#------------------------------------------
def RempliTabReQ():
    compteur=0
    fichierQuestion = ("requetes/alire2.md.txt")
    with open (fichierQuestion, "r") as filin: # j'ouvre la requete comme un objet ( qui sera refermée automatiquement)
        ligne = filin.readline() # création de la variable ligne sous laquelle il y a la méthode filin.readline()
        while ligne != "":
            if ligne[0] == "#":
                compteur=compteur+1
                index='req'+str(compteur)
                dico[index]={}
                question=ligne
                ligne = ""
                requetelu=""
                ligne = filin.readline()
                requetelu =ligne

                while ligne != "\n" and ligne!="": # Tant que ligne n'est pas vide
                    ligne = filin.readline()# lit une ligne du fichier renvoyée sous chaine de caractère
                    requetelu = requetelu + ligne
                ligne=""

                dico[index]['question']=question
                dico[index]['req']=requetelu
            ligne = filin.readline()



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


def afficher_table(fin):
    if fin!=None :
        for row in c.fetchmany(fin):
            print(row[0]) # renvoie lignes
    else:
        for row in c.fetchall():
            print(row[0])

#def projection_table(table,NumColonnes):

#    for row in table:
#        print (row[NumColonnes]))


#------------------------------------------
#Fin bloc fonctions
#------------------------------------------

#Connexion BDD
conn = sqlite3.connect('data/imdb.db') # connection à la base de données
c = conn.cursor() # connection interface, objet cursor


RempliTabReQ()

#affiche tout le dictionnaire
print("affiche tout le dictionnaire")
for key, value in dico.items():
    if isinstance(value, dict):
        for sub_key, sub_value in value.items():
            print(sub_key,sub_value)

print("\n\n")

#affiche les sous element d'une cle
print("affiche les sous element d'une cle")
print(dico['req1'])
print("\n\n")

#affiche une sous cle d'un dictionnaire imbrique de la cle demandée
print("affiche une sous cle d'un dictionnaire imbrique de la cle demandée")
print(dico['req2']['question'])
print("\n\n")


pp = pprint.PrettyPrinter(width=41, compact=True)
pp.pprint(dico['req2']['question'])

#Lit une requete
#requete=lire("req1")
#print(requete)

#execution requete
#result = executer(requete)

#afficher_table()

#ResAff=afficher_table(result)

#Fin de connexion BDD
conn.close()