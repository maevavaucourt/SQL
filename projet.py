import sqlite3 # j'importe le module sqlite3
import pprint

#initialisation des variables
requete = ""
dico = {}

#------------------------------------------
#Bloc de fonctions
#------------------------------------------
def RempliTabReQ():

    """
    Fonction qui charge les requetes dans un dictionnaire ainsi que les questions.
    """

    compteur=0 #intialisation du compteur
    fichierQuestion = ("requetes/alire.md.txt")
    with open (fichierQuestion, "r") as filin: # j'ouvre la requete comme un objet en mode lecture( qui sera refermée automatiquement)
        ligne = filin.readline() # création de la variable ligne sous laquelle il y a la méthode filin.readline()
        while ligne != "": #tant que ligne n'est pas vide
            if ligne[0] == "#": # si le premier caractere de la ligne est #
                compteur=compteur+1 # on ajoute 1 au compteur
                index='req'+str(compteur) #index est une variable qui corrspond au nom de la requete
                dico[index]={}
                question=ligne
                ligne = ""  #on réinitialise la ligne
                requetelu=""
                ligne = filin.readline() # on prend une nouvelle ligne (la suivante)
                requetelu =ligne

                while ligne != "\n" and ligne!="": # tant que la requete n'est pas fini(car apres chaque requete il y a un espace qui est noté "\n")
                    ligne = filin.readline() # lit une ligne du fichier renvoyée sous chaine de caractère
                    requetelu = requetelu + ligne # à la fin on aura la requete entiere
                ligne="" #réinitialisation de ligne

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

def executer(ReqDB):

    """
    Fonction qui execute la requete demandée
    """
    c.execute(ReqDB) # execution de la requete


def afficher_table(fin):

    """
    Fonction d'affichage sur x de ligne demandée
    """

    if fin!=None :
        for row in c.fetchmany(fin): #Affiche les x premiers resultats
            print(row[0]) # renvoie lignes
    else:
        for row in c.fetchall(): #Affiche tout
            print(row[0]) #renvoie lignes

#------------------------------------------
#Fin bloc fonctions
#------------------------------------------

#Connexion BDD
conn = sqlite3.connect('data/imdb.db') # connection à la base de données
c = conn.cursor() # connection interface, objet cursor


RempliTabReQ()

#affiche tout le dictionnaire
#print("affiche tout le dictionnaire")
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

#Lecture d'une requete
requete=lire("req1")
print(requete)

#execution de la requete
result = executer(requete)
print(result)

#Affichage de la table
afficher_table(10)

ResAff=afficher_table(result)

#Fin de connexion BDD
conn.close()
