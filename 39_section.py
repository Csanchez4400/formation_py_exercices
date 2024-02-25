# Importer la bibliothéque
# Localiser le chemin
# Créer un boucle pour chercher les info en d
# Créer les chemins destionation
# créer un boucle pour la creation de dossiers


dictionnaire_films = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}



from pathlib import Path

chemin = Path(r"C:\Users\Owner\Desktop\Udemy Python\Fichiers Py\39_section")

# nom du dossier
# for cle in dictionnaire_films:
# #    print(cle)
# #    print(chemin, cle)
#     chemin_dossier = chemin / cle
# #    print(chemin_dossier)
#     chemin_dossier.mkdir(exist_ok=True)


# nom de sous dossier
#for valeur in dictionnaire_films.get('Employes'):
#    print(valeur)

#print(dictionnaire_films.get('Employes')[0])

#for valeur in dictionnaire_films.values():
#    print(valeur)

#for valeur in dictionnaire_films:
#    print(dictionnaire_films.get('Employes'))


#print(dictionnaire_films.get('Employes'))

for cles, valeurs_liste in dictionnaire_films.items():
#    print(clés, valeurs_liste)
    chemin_dossier2 = chemin / cles
    print(chemin_dossier2)
    chemin_dossier2.mkdir(exist_ok=True)
    for valeurs_unit in valeurs_liste:
#        print(valeurs_unit)
        #print(chemin, clés, valeurs_unit)
        chemin_sous_dossier = chemin / cles / valeurs_unit
        print(chemin_sous_dossier)
        chemin_sous_dossier.mkdir(exist_ok=True)




