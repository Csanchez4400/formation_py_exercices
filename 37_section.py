films = {
    'Le Seigneur des Anneaux' : 12,
    'Harry Potter' : 9,
    'Blade Runner' : 7.5
}

prix = 0

for clé, valeurs in films.items():
    print(clé, valeurs)





for key in films:
    print(films[key])
    prix += (films[key])
    print(prix)

films['Le Seigneur des Anneaux'] = '40'
print(films)


dictionnaire = {"utilisateur": "Paul"}

dictionnaire["utilisateur"] = 'Marie'
dictionnaire['Mot_passe'] = 'Pass45'
print(dictionnaire)