# Aficher les 5 options
choix = ''
liste_courses = []
n = 0

while not (choix) == str(5):
    print('''
Choisissez parmi les 5 options suivantes :
1. Ajouter un élément à la liste de courses
2. Retirer un élément de la liste de courses
3. Afficher les éléments de la liste de courses
4. Vider la liste de courses
5. Quitter le programme
''')

# Demander à l'utilisateur de choisir entre 5 options
    choix = input('\U0001F449 Votre choix : ')




# Ajouter un élément à la liste
    if int(choix) == 1:

        element_ajouter = input('Entrez le nom d\'un élément à ajouter à la liste de course : ')
        liste_courses.append(element_ajouter)
        # Afficher un phase qui va confirmer le l'élément a bien été ajouté
        print(f'L\'élément {element_ajouter} a bien été ajouté à liste.')
        # print(liste_cours)


    # Retirer un élément de la liste
    # Afficher une phase pour : Votre choix : 2
    # Afficher un phase qui va confirmer le l'élément a bien été rétiré
    # Affficher une phase pour mentionner que l'élément à rétirer ne se trouve pas dans la liste
    if int(choix) == 2:
        element_retirer = input('Entrez le nom d\'un élément à retirer de la liste de courses : ')
        if element_retirer not in liste_courses:
            print(f'L\'élément {element_retirer} n\'est pas dans la liste.')
        else:
            liste_courses.remove(element_retirer)
            print(f'L\'élément {element_retirer} a bien été suprimé de la liste.')


    # Afficher la liste
    # Afficher une phase pour : Votre choix : 3
    # Afficher un phase qui va confirme le choix de voir la liste
    # Afficher un message pour dire que la liste ne contient pas aucun élément
    if int(choix) == 3:
        if liste_courses == []:
            print('Votre liste ne contient aucun élément.')
        else:
            print('Voici le contenu de votre lsite : ')
            for i in liste_courses:
                n += 1
                print(f'{n}.{i}')


    # Vider le contenue de la liste
    if int(choix) == 4:
        liste_courses.clear()
        print('La liste à été vidée de son contenu')

    # Afficher une phase pour : Votre choix : 4
    # Afficher un phase qui va confirmer la liste a été vidée

    # Afficher un phase pour quitter : À bientôt
    if int(choix) == 5:
        print('À bientôt')

    continue











