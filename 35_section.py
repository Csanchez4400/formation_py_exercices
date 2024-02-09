import json
import sys

chemin_fichier = r"C:\Users\Owner\Desktop\Udemy Python\Fichiers Py\list_cours_bd.json"
with open(chemin_fichier, 'r') as f:
    donnees = json.load(f)

liste = [donnees]
options = ""

while True:

    options = input(
        "\n\nQue souhaitez vous faire: \n\n1) Ajouter un article à la liste\n2) Retirer un article de la liste\n3) Afficher la liste\n4) Vider la liste\n5) Quitter le programme\nEntrez votre choix: ")

    if options.isdigit() == False:
        print("\nENTREZ UNE OPTION VALIDE")

    elif options == "1":
        #ajout = input("\nQue souhaitez vous ajouter? : ")
        #liste.append(ajout)
        #print(f"\n\n{ajout} à bien été ajouté à la liste")
        ajout = input("\nQue souhaitez vous ajouter? : ")

        #with open(chemin_fichier, 'r') as f:
        #    donnees = json.load(f)

        donnees.append(ajout)

        with open(chemin_fichier, 'w') as f:
            json.dump(donnees, f, indent=4)

        print(f"\n\n{ajout} à bien été ajouté à la liste")




    elif options == "2":
        #retire = input("\nQue souhaitez vous retirer de la liste? : ")
        #if retire in liste:
        #    liste.remove(retire)
        #    print(f"\n{retire} à bien été retiré de la liste")
        #else:
        #    print(f"\n{retire} n'est pas dans la liste")

        retire = input("\nQue souhaitez vous retirer de la liste? : ")
        if retire in donnees:
            donnees.remove(retire)
            with open(chemin_fichier, "w") as f:
                json.dump(donnees, f, indent=4)


            print(f"\n{retire} à bien été retiré de la liste")
        else:
            print(f"\n{retire} n'est pas dans la liste")






    elif options == "3":
        if len(donnees) >= 1:
            for i, item in enumerate(donnees):
                print(f"\n{i + 1}. {item}")
        else:
            print("\nVotre liste est vide")

    elif options == "4":
        #liste.clear()
        #print("\nLa liste à été vidée de son contenu")
        donnees.clear()
        with open (chemin_fichier, 'w') as f:
            json.dump(donnees, f, indent=4)
        print("\nLa liste à été vidée de son contenu")




    elif options == "5":
        print("\nÀ bientôt")
        sys.exit()