import sqlite3 # j'importe le module sqlite3
import pprint
import tkinter
import os


#initialisation des variables
requete = ""
dico = {}

#------------------------------------------
#Bloc de fonctions
#------------------------------------------
def RempliTabReQ():

    """
    Fonction qui charge les requetes dans un dictionnaire ainsi que les questions.
    Argument :
        Aucun
    Renvoi:
        Rien
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


def lirequestion(question):
    """
    Fonction qui lit la question demandée.
    Arugument:
        NomRequete : chaine de caarctère correspondant à une question.
    Renvoi:
        La question demandée.

    """

    fichier = (NomRequete) + ".sql"
    with open ("requetes/" + fichier, "r") as filin: # j'ouvre la requete comme un objet ( qui sera refermée automatiquement)
        requetelu = ""
        ligne = filin.readline() # création de la variable ligne sous laquelle il y a la méthode filin.readline()
        if ligne[0] == "#":
            question = ligne
        return question

def lirerequete(NomRequete):
    """
    Fonction qui lit la requete demandée.
    Arugument:
        NomRequete : chaine de caarctère correspondant à une requete.
    Renvoi:
        L'écriture de la requete SQL demandée.

    """

    fichier = (NomRequete) + ".sql"
    with open ("requetes/" + fichier, "r") as filin: # j'ouvre la requete comme un objet ( qui sera refermée automatiquement)
        requetelu = ""
        ligne = filin.readline() # création de la variable ligne sous laquelle il y a la méthode filin.readline()
        if ligne[0] == "#":
            ligne = filin.readline()
        requetelu = ligne
        while ligne!= "": # Tant que ligne n'est pas vide
            ligne = filin.readline()# lit une ligne du fichier renvoyée sous chaine de caractère
            requetelu = requetelu + ligne
        return requetelu


def executer(ReqDB):

    """
    Fonction qui execute la requete demandée
    Argument:
        ReqDB: c'est la requete qui a été lu
    Renvoi:
        Rien
    """
    c.execute(ReqDB) # execution de la requete


def afficher_table(fin,Maxi):

    """
    Fonction d'affichage sur x de ligne demandée
    Argument:
        fin: nombre correspondant au nombre de lignes affichées
    Renvoi:
        Le resultat de la requete
    """
    final=""
    final = separation(Maxi)
    if fin!=None :
        for row in c.fetchmany(fin): #Affiche les x premiers resultats
            inter ="|"+row[0]+" "*(Maxi-len(row[0]))+"|" # |title   |
            final=str(final)+str(inter) + str(separation(Maxi))
    else:
        for row in c.fetchall(): #Affiche tout
            inter ="|"+row[0]+" "*(Maxi-len(row[0]))+"|" # renvoie lignes
            final=str(final)+str(inter) + str(separation(Maxi))
    return final


def separation(longSep):

    sep=chr(10)+"+"+"-"*(longSep)+"+"+chr(10) #+-------+
    return sep

def longChaine(Req,fin):
    Longch=0
    Maxi=0
    if fin!=None :
        for row in c.fetchmany(fin): #Affiche les x premiers resultats
            Longch= len(row[0])
            if Maxi <Longch:
                Maxi = Longch

    else:
        for row in c.fetchall(): #Affiche tout
            Longch= len(row[0])
            if Maxi <Longch:
                Maxi = Longch

    return Maxi

def affichage(texte, titre = "Requêtes tables"):
	"""
	Affiche un texte (résultat d'une requête)
	dans une fenêtre tkinter
	Auteurs: M CHOUCHI
	Arguments:
		texte: str du texte à afficher
		titre: str du titre de la fenêtre
	Renvoi:
		rien
	"""
	root = tkinter.Tk()
	root.title(str(titre))
	RWidth=root.winfo_screenwidth() - 100
	RHeight=root.winfo_screenheight() - 100
	root.geometry("%dx%d+50+0"%(RWidth, RHeight))
	text=tkinter.Text(root, wrap = 'none')
	scroll_x=tkinter.Scrollbar(text.master, orient='horizontal', command = text.xview)
	scroll_x.config(command = text.xview)
	text.configure(xscrollcommand = scroll_x.set)
	scroll_x.pack(side = 'bottom', fill = 'x', anchor = 'w')
	scroll_y = tkinter.Scrollbar(text.master)
	scroll_y.config(command = text.yview)
	text.configure(yscrollcommand = scroll_y.set)
	scroll_y.pack(side = tkinter.RIGHT, fill = 'y')
	text.insert("1.0", texte)
	text.pack(side = tkinter.LEFT, expand = True, fill = tkinter.BOTH)
	root.mainloop()

#------------------------------------------
#Fin bloc fonctions
#------------------------------------------

#Connexion BDD
conn = sqlite3.connect('data/imdb.db') # connection à la base de données
c = conn.cursor() # connection interface, objet cursor


RempliTabReQ()

#affiche tout le dictionnaire
##print("affiche tout le dictionnaire")
##for key, value in dico.items():
##    if isinstance(value, dict):
##        for sub_key, sub_value in value.items():
##            print(sub_key,sub_value)

#print("\n\n")

#affiche les sous element d'une cle
#print("affiche les sous element d'une cle")
#print(dico['req1'])
#print("\n\n")

#affiche une sous cle d'un dictionnaire imbrique de la cle demandée
##print("affiche une sous cle d'un dictionnaire imbrique de la cle demandée")
##print(dico['req2']['question'])
##print("\n\n")


#pp = pprint.PrettyPrinter(width=41, compact=True)
#pp.pprint(dico['req1']['question'])

#requetes
NomRequete = "req1"

#Lecture d'une requete
question = lirequestion(NomRequete)
print(question)

requete=lirerequete(NomRequete)
print(requete)

#Nombre enregistrements
NbEnregistrement= 10


#execution de la requete
result = executer(requete)

Maxi = longChaine(requete,NbEnregistrement)

result = executer(requete)
#Affichage de la table
tabReq = afficher_table(NbEnregistrement,Maxi)
print(tabReq)

texte = str(requete) + 2*chr(10) + str(question)  + str(tabReq)

affichage(texte,titre = "Requêtes tables")
#Fin de connexion BDD
conn.close()
