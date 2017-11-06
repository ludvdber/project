""" 
    Projet 1: BlackJack
    Un joueur contre la banque
"""

__author__ = "Ludovic Vanden Berghe"
__date__ = "11 octobre 2017"


from random import randint, seed

dico = {'1':'as', '11':'valet', '12':'dame', '13':'roi'}
choix = 1       #1: recommence une partie, 2: arrête la partie 

#Début de l'échange avec l'utilisateur

print("Bienvenue au Blackjack")
graine=int(input("Entrez la graine : "))
seed(graine)
mon_argent = int(input("Veuillez entrer la quantité d'argent en votre possession : " ))

while choix == 1: #boucle pour relancer une partie
    mise = int(input( "Veuillez entrer votre mise (vous avez : "+str(mon_argent)+") : "))
    mon_argent = mon_argent - mise
    piocher = 1 #1: oui, 2: non
    points_joueur = 0
    points_banque = 0
    points_carte = 0
    nbre_pioche_joueur = 0
    nbre_pioche_banque = 0
    As = 0
    while piocher == 1: #boucle pour piocher une carte
        carte = randint(1, 13)
        nbre_pioche_joueur += 1
        if carte == 1 : #le cas de l'As, lui donne la valeur 1 pour le moment
           points_carte = 1
           As = 1
        if carte > 10 and carte != 1: #dame, valet ou roi = 10 points
            points_carte = 10

        else:
            points_carte = carte
            
        points_joueur += points_carte
        nom_carte = dico.get(str(carte), carte)
        print("La carte tirée est : "+str(nom_carte))

        if points_joueur > 21:
            piocher = 2 #stop la partie
            print("Vous avez sauté\n")
            
        else:
            piocher = int(input("Souhaitez-vous une carte ? (1: oui, 2: non) "))
    if As == 1:
        if points_joueur <= 11:
            points_joueur += 10 #l'As avait une valeur de 1, en faisant +10 il a la valeur de 11 qui permet un avantage
    if points_joueur <= 21:
        print("Vous avez obtenu "+str(points_joueur)+" points")

    #*** Code pour la banque ***#
        
        print("La banque joue :")
        carte = 0
        As = 0    
        while points_banque < 17: #si la somme des cartes est inférieures à 17, on continue
            carte = randint(1, 13)
            nbre_pioche_banque += 1
            if carte == 1: #le cas de l'As, lui donne la valeur 1 pour le moment
               points_carte = 1
               As = 1
            if carte > 10 and carte != 1: #dame, valet ou roi = 10 points
                points_carte = 10

            else:
                points_carte = carte
            
            points_banque += points_carte
            nom_carte = dico.get(str(carte), carte)
            print("La carte tirée est : "+str(nom_carte))
            
        if As == 1:
            if points_banque <= 11:
                points_banque += 10
        if points_banque > 21:
            print("La banque a sauté")
            print("Vous gagnez "+str(mise)+"\n")
        else:
            print("La banque a obtenu "+str(points_banque)+" points")

            if points_joueur > points_banque:
                print("Vous gagnez "+str(mise)+"\n")
                mon_argent += mise*2
            elif points_banque > points_joueur:
                print("La banque gagne\n")
                
            elif points_banque == 21 and point_joueur == 21: #Vérification d'un BlackJack du joueur et/ou de la banque
                if nbre_pioche_joueur < nbre_pioche_banque:
                    print("Vous gagnez "+str(mise)+"\n")
                    mon_argent += mise*2
                elif nbre_pioche_joueur > nbre_pioche_banque:
                    print("La banque gagne\n")
                else:
                    print("Égalité\n")
            else:
                print("Égalité\n")

    choix = int(input("Souhaitez-vous jouer une autre partie ? (1: oui, 2: non) "))
