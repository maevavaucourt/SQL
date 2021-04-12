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
        table += "<tr><td>\n"+str(row[0])+str(row[1]) + "</td></tr>\n"
    table +="</table>\n"
    print(table)
    finhtml()

sql= "SELECT DISTINCT titleType FROM title_basics"

execute_sql(conn,sql)
