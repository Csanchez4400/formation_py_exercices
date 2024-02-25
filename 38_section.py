from pathlib import Path

#########
# importer la bibliothéque pathlib
# se situer sur le chemain ou se trouve le dossier avec les fichiers
# creer les dossier si existent : Musique / Videos / Images / Documents / Divers
# Creer une sequence qui va analizer chaque fichier
# La sequence doit analyser les extentions
# La sequence passe à travers les fichier et les mets dans le bon dossier

dossier_initial = Path(r'C:\Users\Owner\Downloads\38_Test_py')
print(dossier_initial)
liste_dossier = [
    'Musique',
    'Videos',
    'Images',
    'Documents',
    'Autres'
]

for i in liste_dossier:
    dossier_final = dossier_initial / i
    dossier_final.mkdir(exist_ok = True)
    print(i)

print('-' * 100)
# for x in dossier_initial.iterdir() :
#     print(x)
#
# print('-' * 100)
#
# for g in dossier_initial.glob('*.pdf'):
#     print(g.name)
#     print(g.suffix)
#
# print('-' * 100)

for u in dossier_initial.iterdir():
    if u.suffix == '.pdf':
        print(u)
        #    u = u.parent.parent / (u.stem + "\Documents" + u.name + u.suffix)
        u = u.parent / (u.parent + "\Documents" + u.stem + u.suffix)
        print(u)
    #    print(u)

print('-' * 100)
