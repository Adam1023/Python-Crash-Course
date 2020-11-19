import sys
from random import randint

######################################################################################################################
# Ce qui se trouve ici en dessous, c'est le lancement du jeu.
# Je demande à l'utilisateur d'entrer son nom et si le nom est bon d'entrer un mdp.
# Puis le jeux commence.
# Mais si le nom ou le mdp est faux le programme s'arrête.
# Pour info le nom c'est Adam et le mdp 1234.

# Lance le programme maintenant pour comprendre ce qui se passe. Et puis regarde le code ici en dessous et essaye de
# comprendre ce que j'ai fait.
# Essaye de faire des fautes dans le nom, puis dans le mdp.
# Une fois que t'as compris, change ce nom et mdp en quelque chose d'autres dans le programme. Genre au lieu de Adam
# tu mets zaghlol ou quoi .... comme tu veux.
# Ensuite plus bas il y aura les fonctions que tu dois implémenter !


name = input("Name: ")

if name == "Adam":
    password = int(input("Password: "))
    if password == 1234:
        input("Welcome to the game ! Are you ready ?? ")
        print("######################################")
        print("     ############################")
        print("          ##################")
        print("               ########")
        flous = int(input("Combien veux-tu miser (en euro)? "))


    else:
        print("Faux ! héhé")
        sys.exit()  # Cette ligne permet de quitter le programme, même s'il y a encore des bouts de codes en dessous

else:
    print("Dégage vieux type !")
    sys.exit()  # Cette ligne permet de quitter le programme, même s'il y a encore des bouts de codes en dessous

# Donc mtn il existe 3 variables. Les variables "nom" et "password" qui contiennent le nom et mdp de l'utilisateur.
# Cette variable n'a plus d'importance, on ne l'utilisera plus.
# La variable importante dans tout ce qu'il y a au dessus, c'est la variable "flous", que tu vas devoir utiliser plus
# bas.
######################################################################################################################


input("A partir d'ici, c'est à toi de jouer mec ! ")  # Retire cette ligne de code quand tu auras compris


##################################
#####  1) LES FONCTIONS     ######
##################################

def generate_new_list():
    """
    Cette fonction renvoi une nouvelle liste contenant 10 éléments, tous générés de façon random.
    Elle n'a pas besoin de paramètres, voilà pourquoi il n'y a rien entre parenthèse.
    C'est tout simplement une nouvelle liste qui sera ranvoyée (return)

    Pour ceux qui ne savent pas comment le module random fonctionne:
    Si vous montez tout à fait en haut vous verrez "from random import randint". Cela veut dire qu'on a importé le
    module random dans ce programme python. Mais pas tout le module. Uniquement la fonction randint().
    Cette fonction (randint(x,y)) retourne un chiffre qui se situe entre x et y (x et y sont compris).
    Par exemple si j'écris randint(1,9) dans la console, la réponse sera un chiffre au hasard entre 1 et 9 (après avoir
    importé cette fonction bien sûr). SI je refais randint(1,9), la console me donnera un autre chiffre au hasard
    (ou le même) etc.

    :return: Une liste contenant 10 chiffres générés au hasard entre 1 et 30.
    """

    # Pour générer une nouvelle liste, on initialise d'abord une variable contenant une liste vide
    liste_de_chiffres = []

    # Puis j'utilise une boucle for pour boucler exactement 10 fois.
    # On boucle dix fois et i incrémente de 1 à chaque fois en commencant de 0 jusqu'à 9 (compris).
    # La variable i n'est pas importante, tout ce qu'on veut c'est boucler 10 fois. A chaque nouvelle boucle on génère
    # un nouveau chiffre de façon random et on donne ce nouveau chiffre à la variable "chiffre_random".
    # Ensuite ce chiffre est ajouté à la liste.
    # Regarde le code et essaye de comprendre:
    for i in range(10):
        chiffre_random = randint(1, 30)

        # While suivante est importante pour éviter une répétition du même chiffre. C'est pas grave si tu comprends pas:
        while chiffre_random in liste_de_chiffres:
            chiffre_random = randint(1, 30)

        liste_de_chiffres += [chiffre_random]

    # A la fin de la boucle la liste contiendra 10 chiffres entre 1 et 70. Et à chaque fois qu'on appellera cette
    # fonction à nouveau dans le programme, une nouvelle liste sera générée.

    # Maintenant il ne reste plus qu'à renvoyer cette liste (en dehors de la boucle for bien évidemment)
    return liste_de_chiffres


# A partir d'ici, tu dois implémenter les fonctions restantes:


def value_is_in_list(chiffre, liste):
    """
    Cette fonction vérifie si un certain chiffre se trouve bien dans une certaine liste. Cette fonction est une
    fonction booléenne. Cela veut dire qu'elle renvoi soit True (si le chiffre se trouve dans la liste), soit False
    (si le chiffre ne se trouve pas dans la liste).

    Cette fonction peut être implémenté facilement en utilisant l'opérateur "in". Mais ce serait bête de le faire car tu
    ne t'entraîneras pas de cette façon.

    Voici comment tu dois procéder:
    Tu vérifies chaque éléments de la liste. Si un élément est le même que le chiffre, alors tu return True.
    S'il est passé sur chaque élément et qu'aucun est le même que le chiffre, tu return False.

    :param chiffre: contient un int qui est l'objet de la vérification
    :param liste: contient une liste de int
    :return: True si le chiffre se trouve dans la liste, sinon False.
    """
    return chiffre in liste


def supprime_element_de_liste(element, liste):
    """
    Cette fonction renvoi (return) une nouvelle liste, qui contient tous les éléments de "liste", sauf celle qui est
    égale à élément. Tu peux assumer que "element" sera toujours un element de la liste "liste".

    Pour implémenter cette fonction, tu dois utiliser l'indexation. Et donc retourner une nouvelle liste qui contient
    tous les éléments de "liste" sauf celle à la position ou se trouve l'élément à supprimer.

    :param element: l'élément à supprimer de la liste (c'est un int)
    :param liste: la liste qui contient l'élément à supprimer
    :return: une nouvelle liste identique à "liste", mais sans "element"
    """
    liste2 = []
    for elem in liste:
        if elem != element:
            liste2.append(elem)

    return liste2


def is_game_over(money, liste):
    """
    Cette fonction est une fonction booléenne qui recoit comme paramètre "money" (c'est à dire l'argent restant) et une
    "liste", qui est donc la liste contenant les chiffres restants à deviner.
    Si il n'y a plus d'argent ou que la liste est vide, alors cette fonction doit renvoyer True. Sinon False.
    """
    return money < 0 or len(liste) == 0


##################################
##### 2) DEMARRAGE DU JEU   ######
##################################
"""
C'est ici que tu dois implémenter ton jeu en te basant sur les fonctions que tu as fait.
1) Tout d'abord on génère une nouvelle liste et on la donne comme valeur à la variable "liste_de_chiffres".
2) Ensuite on implémente la while. On sort de la while que si il n'y a plus de flous ou que la liste est vide.
    3) On demande en boucle d'entrer un chiffre en input et on vérifie si le chiffre se trouve dans la liste à l'aide de 
    la fonction "value_is_in_list" que t'as du implémenter
        *   S'il s'y trouve, on supprime ce chiffre de la liste à l'aide de la fonction "supprime_element_de_liste()"
            et on calcule le nombre de chiffres restants (= longueur de la liste) et on print ce qu'il faut printer.

        *   S'il ne s'y trouve pas on retire la moitiée de l'argent et on print ce qu'il faut printer.

4) On vérifie, en dehors de la while, si le joueur a gagné ou s'il a perdu.
"""

def start_game():
    global flous

    # 1)
    liste_de_chiffres = generate_new_list()

    # 2)
    while is_game_over(flous, liste_de_chiffres) == False:
        chiffre_choisis = int(input("Devine un chiffre: "))

        # 3)
        if value_is_in_list(chiffre_choisis, liste_de_chiffres) == True:
            liste_de_chiffres = supprime_element_de_liste(chiffre_choisis, liste_de_chiffres)
            nombre_chiffres_restants = len(liste_de_chiffres)
            print("Félicitation, Il ne vous reste plus que", nombre_chiffres_restants, "chiffres à deviner.")

            flous += flous // 10  # L'argent précédent + un dixième de l'argent (//--> pour éviter virgules)
            print("Votre cash est désormais de", flous, "euro")

        elif value_is_in_list(chiffre_choisis, liste_de_chiffres) == False:
            flous = flous - flous // 10
            print("Manqué, il vous reste", flous, "euro !")

            nombre_chiffres_restants = len(liste_de_chiffres)
            print("Et il vous reste toujours", nombre_chiffres_restants, "chiffres à deviner")

    # 4)
    if flous <= 0:
        print("Haha, tu vois pourquoi le Lotto c’est hram maintenant ?!")
        print("Aller, va dormir dans la rue !")

    elif len(liste_de_chiffres) == 0:
        print("T'as tout trouvé, mais ... ayaaa, tu viens de jouer au lotto, tu hchem pas ?!")









# Et bien sûr, il faut démarrer le jeu:
start_game()