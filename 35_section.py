import sys

liste = []
options = ""

while True:

    options = input(
        "\n\nQue souhaitez vous faire: \n\n1) Ajouter un article à la liste\n2) Retirer un article de la liste\n3) Afficher la liste\n4) Vider la liste\n5) Quitter le programme\nEntrez votre choix: ")

    if options.isdigit() == False:
        print("\nENTREZ UNE OPTION VALIDE")

    elif options == "1":
        ajout = input("\nQue souhaitez vous ajouter? : ")
        liste.append(ajout)
        print(f"\n\n{ajout} à bien été ajouté à la liste")

    elif options == "2":
        retire = input("\nQue souhaitez vous retirer de la liste? : ")
        if retire in liste:
            liste.remove(retire)
            print(f"\n{retire} à bien été retiré de la liste")
        else:
            print(f"\n{retire} n'est pas dans la liste")

    elif options == "3":
        if len(liste) >= 1:
            for i, item in enumerate(liste):
                print(f"\n{i + 1}. {item}")
        else:
            print("\nVotre liste est vide")

    elif options == "4":
        liste.clear()
        print("\nLa liste à été vidée de son contenu")

    elif options == "5":
        print("\nÀ bientôt")
        sys.exit()