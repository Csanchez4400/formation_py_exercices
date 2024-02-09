import random


print('''
🏯🏯🏯 Donjons et Dragons 🐉🐉🐉
''')



vie_heros = 50
vie_ennemie = 50
nombre_potions = 3
options_possibles = [1, 2]



while vie_heros > 0:

    choix_heros = input('Souhaitez-vous attaquer (1) ⚔️ ou utiliser une potion (2) ? 🧪 : ')

    if (choix_heros.isdigit() == False) or (int(choix_heros) not in options_possibles):
        print('️🤦‍♀️ L\'option n\'est pas valide🤦. Veillez attaquer (1) ⚔️ ou utiliser une potion (2) 🧪.' )
        print('-' * 100)
        continue


    if int(choix_heros) == 1:

        valeur_attaque_heros = random.randint(5, 10)
        vie_ennemie = vie_ennemie - valeur_attaque_heros

        print(f'💥💥🦸🦸 Vous avez infligé {valeur_attaque_heros} points de dégats à l\'ennemie. 💥💥')
        if vie_ennemie <= 0:
            print('''🏆🏆🎖️🎖️ Tu as gagné🏆🏆🎖️🎖️ 
Fin du jeu.''')
            break

    elif int(choix_heros) == 2:

        if nombre_potions != 0:
            nombre_potions -= 1

            valeur_potion_vie = random.randint(15, 50)
            vie_heros = vie_heros + valeur_potion_vie
            # Si je choisi une potion, la phase : Vous récupérez x points de vie. (x potions restantes)
            print(f'Vous récupérez {valeur_potion_vie} ({nombre_potions} potions restants 🧪 ❤️❤️❤️)')
        else:

            print('Vous n\'avez plus de potions 😩😩😩')

            continue


    valeur_attaque_ennemie = random.randint(5, 15)
    vie_heros = vie_heros - valeur_attaque_ennemie

    print(f'🧿🧿🧟L\'ennemie vous a infligé {valeur_attaque_ennemie} points de dégats.🧿🧿')
    if vie_heros <= 0:
        print('''🩻🩻🩻 L\'heros est mort 🩻🩻🩻🩻
Fin du jeu.''')
        break



    print(f'Il vous reste {vie_heros} points de vie. ❤️❤️❤️')
    print(f'Il reste {vie_ennemie} points de vie à l\'ennemie. 💙💙💙')
    print('-' * 100)




    if int(choix_heros) == 2:
        print('Vous passez votre tour ...😨😨😨')
        valeur_attaque_ennemie = random.randint(5, 15)
        vie_heros = vie_heros - valeur_attaque_ennemie
        print(f'🧿🧿🧟 L\'ennemie vous a infligé {valeur_attaque_ennemie} points de dégats.🧿🧿')

        if vie_heros <= 0:
            print('''🩻🩻🩻 L\'heros est mort 🩻🩻🩻
Fin du jeu.''')
            break

        print(f'Il vous reste {vie_heros} points de vie.❤️❤️❤️')
        print(f'Il reste {vie_ennemie} points de vie à l\'ennemie.💙💙💙')
        print('-' * 100)