# Créé par Elève, le 04/05/2021 en Python 3.4

M = [[0]*7 for i in range(6)]
print(M)

def jouer():
    nb_colonne = int(input("Dans quelle colonne voulez vous mettre votre jeton ?"))
    while nb_colonne < 0 or nb_colonne > 7:
        print("La colonne", nb_colonne,"n'existe pas !")
        nb_colonne = int(input("Dans quelle colonne voulez vous mettre votre jeton ?"))
    i = 5
    j = nb_colonne
    while M[i][j] == 0 and i != -1:
        i = i -1
    return i

def colonne_pleine(nb):
    if nb == -1:
        print("La colonne est pleine !")

#def inserer(nb,)



nb = jouer()
colonne_pleine(nb)
print(nb)