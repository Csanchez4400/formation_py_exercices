import random



print('''
*** Le jeu de nombre mystère ***
''')

nombre_aleatoire = random.randint(1, 100)
essais = 5
boucles_while = 1
#print(nombre_aleatoire)


print(f'Il te reste {essais} essais')
nombre_client = input('Devine le nombre : ')


while (nombre_client != str(nombre_aleatoire)):
    if nombre_client.isdigit():
        essais -= 1
        boucles_while += 1

        if nombre_aleatoire < int(nombre_client):
            print(f'Le nombre mistère est plus petit que {nombre_client}')


        elif nombre_aleatoire > int(nombre_client):
             print(f'Le nombre mistère est plus grand que {nombre_client}')


        if essais != 0:
            print(f'Il te reste {essais} essais')
            nombre_client = input('Devine le nombre : ')

        else:
        # Si je devine pas, afficher le message : Dommage ! Le nombre mistère était xxx
            print(f'''Dommage ! Le nombre mistère était {nombre_aleatoire}
Fin du jeu.''')
            break

    else:
        print('Veiller entrer un nombre valide.')
        print(f'Il te reste {essais} essais')
        nombre_client = input('Devine le nombre : ')


if nombre_client == str(nombre_aleatoire):
    print(f'''Bravo ! Le nombre mistère était bien {nombre_aleatoire}!
    Tu as trouvé le nombre en {boucles_while} essais 
    Fin du jeu.
        ''')






