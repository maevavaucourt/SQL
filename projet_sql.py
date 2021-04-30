#!"C:\winpython\python-3.8.5.amd64\python.exe"

import sqlite3
def database_connexion(db_file):
    """
    créer une connexion à une base de données SQLite spécifiée par le db_file
    : param db_file: fichier de base de données
    : return: Objet de connexion ou Aucun
    """
    connexion = None
    try:
        connexion = sqlite3.connect(db_file)
    except Error as e:
        return e

    return connexion
conn=database_connexion("data/imdb.db")

def debuthtml():
    print("Content-type: text/html")
    print("\n")
    print("<html><head>")
    print("\n")
    print(" <style> table, th, td {border: 1px solid black;  padding: 5px; border-collapse: collapse;} </style> ")
    print("</head><body>")

def finhtml():
    print("</body></html>")

def execute_sql(connexion,sql):
    cur = connexion.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    debuthtml()
    table = "<table>\n"
    for row in rows:
        table += "<tr><td>\n"+str(row[0]) + "</td></tr>\n"
    table +="</table>\n"
    print(table)
    finhtml()

def charger(NomRequete):
    fichier = (NomRequete) + ".sql"
    with open ("requetes/" + fichier, "r") as filin:
        requete = ""
        ligne = filin.readline()
        if ligne[0] == "#":
            ligne = filin.readline()
        requete = ligne
        while ligne!= "":
            ligne = filin.readline()
            requete = requete + ligne
        return requete

def longueur(sql):
    rows = cur.fetchall()
    for row in rows :
        print(len(row(0)))

NomRequete = "req2"


sql= charger(NomRequete)
print(longueur(sql))

execute_sql(conn,sql)

