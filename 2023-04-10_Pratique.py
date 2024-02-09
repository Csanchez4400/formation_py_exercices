# TYPES
    # str
a = "Tibu"
print(type(a))

    # int
b = 12 # Entiers

    #Tuple
c = 12,1 # Décimale
d = 0,98
print(type(c), type(d))

    # Foat
e = 1.555 # Décimale
print(type(e))

    # Bool
i = True
print(type(i))



# MANIPULER UNE CHAÎNE DE CARACTÈRES 
    # upper()
j = "Bilan".upper() # Super important de mettre les paranthèse
print(j)

    # lower ()
k = "ManiPuLer".lower()
print(k)

    # replace("", "")
p = "Formatage".replace("age","AGE")
print(p) # Remplace une chaîne de caractères par une autre


    # capitalize()
r = "avec".capitalize()
print(r)

    # zfill(int)
s = "S".zfill(3)
print(s) # Lé résultat est 00S. Il va ajouter de 0 dans une chaîne de caractères. Mais, il va compter la quantité de chaîne de caractères avec le numéro que nous avons saisi. 

    # .joint("")
v = "Wikipedia".join(",,,,,,")
print(v) # Prend la lettre ou la chaîne de catactères un par un et l'ajoute au mot. 

    # title()
w = "robot".title()
print(w)

    # strip ()
x = "       Fonctions     ".strip() # Elimine les espaces
y = "Fonctions".strip("ions") # Elimine les mots mentionnés
print(x) 
print(y)



# QUESTIONNAIRE UNE CHAÎNE DE CARACTÈRES
    # find("")
l = "Variables".find("bles") # Super important de mettre les mots entre "" 
print(l) # Le résultat est 5. Il y a 5 chaînes de caractères avant le mot "bles"

    # count("")
m = "Conventions".count("n")
print(m) # le résultat est 3. Combiens fois la lettre "n" apparise 

    # startwith("")
q = "Opérateurs".startswith("Opé")
print(q) # Le résultat est True. Il vérifie si la chîne de caractères commence par "Opé"

    # isdigit()
t = "78".isdigit()
u = "Set".isdigit()
print(t) # True. C'est un nombre entier ? 
print(u) #  False



# AFFECTATION DE VARIABLES
     # Simple
aa = 5
aa = 6.3

    # Paralleles
bb, cc, dd, ee = 4, 5, 8, 7
print(dd) 


    # Multiples
ff = gg= hh = 9

# OPÉRATEURS MATHÉMATIQUES

    # / 
print(10/5)

    # //
print(10//5) # Division entier
     
    # *
print(10*5)

    # **
print(10**5) # Puissance

    # %
print(10%8) # Recuperer le reste d'un division (10/8=1.25). Résultat = 2

    # < >

    # <=   >= 

    # == 
    # Attention ! = c'est pour affecter une variable. == C'est égale à. 

    # =!



# FORMATAGE CHAÎNE DE CARACTÈRES
    # f-string 
    # Action qui nous permet d'inclure des texte comme une variable
username = "Ramon"
f"Bonjour {username}, vous êtes connecté à votre portail"

print(f"Bonjour {username}, vous êtes connecté à votre portail")

ff = 5
gg = 15

f"La multiplication du nombre {ff} et du nombre {gg} est la valeur de {ff*gg}"

print(f"La multiplication du nombre {ff} et du nombre {gg} est la valeur de {ff*gg}")



# INPUT
premier_nombre = int(input("Saisir première nombre "))
deuxieme_nombre = int(input("Saisir un deuxième nombre "))
print(f"La division entre {premier_nombre} et {deuxieme_nombre}, c'est {premier_nombre / deuxieme_nombre}")

# STRUCTURES CONDITIONNELLES = ALGORITHMES
    # IF - ELIF - ELSE

savings = int(input("Valeur totale des éparners dans ton compte bancaire "))
if  savings >= 40000:
    print("La banque peut te preter 150 000")
elif 20000 <= savings < 40000:
    print("La banque peut te preter 100 000")
else:
    print("Ta demande de prêt est réfusé")

    # AND - OR - NOT
usernameadmin = input("Saisir votre nom ")
motdepasse = input("Saisir votre mot de passe ")
if usernameadmin == "admin" and motdepasse == "admin123":
    print("Vous êtes connecté en tant qu'utilisateur")
elif not usernameadmin == "admin" and not motdepasse == "admin123":
    print("Connexion interdit. Vous n'êtes pas l'admin.")



# LES ERREURS
    # Syntaxe
    # Exécution
    # Sémantique


# LISTES
    # Listes
liste1 = ["Francia", "Alemania", "Egipto"]
liste2 = [1,2,3,4]
print(liste2)

    # Tuples 
    # Listes que nous ne pouvons pas modifier. 
mon_tuple =  (1, 2, 3)
print(mon_tuple)

    





# QUESTIONNER  UNE LISTE
    # INDICE LISTE
liste1 = ["Francia", "Alemania", "Egipto"]
print(liste1[0])

    # "text" in "Liste"       # "text" not in "Liste"
liste89 = ["Francia", "Alemania", "Egipto"]
print("Egipto" in liste89) # True. Vérifier si l'élément se trouve dans la liste. 

    # len()
print(len("Camerun"))
print(len(["Francia", "Alemania", "Egipto"])) # Compte la quantité d'éléments

    # round()
print(round(4,8))

    # min()
print(min([45, 56, 98, 23, 98]))
print(min("Camerun"))

    # max()
print(max([45, 56, 98, 23, 98]))
print(max("Camerun"))

    # sum()
print(sum([45, 56, 98, 23, 98]))




# MODIFIER UNE LISTE
    #split()
liste3 = "Tout, ce dont tu as besoin".split() # Nous allons prendre une chaîne de caractères et la changer à une liste. 
print(liste3) # ['Tout,', 'ce', 'dont', 'tu', 'as', 'besoin']

    # .join([liste])
liste04 = ", ".join(["Francia", "Alemania", "Egipto"]) # Nous allons prendre une liste pour la changer à une chaîne de caractères. 
print(liste04)


    # liste[indice] = Modification
liste1 = ["Franccccccia", "Alemania", "Egipto"]
liste1[0] = "Francia"
print(liste1) 

    # liste.append("text")
liste8 = ["Francia", "Alemania", "Egipto"]
liste8.append("Camerun") # ajouter qqch
print(liste8)

    # liste.extend([])
liste98 = ["Francia", "Alemania", "Egipto"]
liste98.extend([45, 56, 98, 23, 98]) # Ajouter plusiuers éléments d'un coup à une liste
print(liste98)

    # del liste[indice]
liste66 = ['Francia', 'Alemania', 'Egipto', 'Camerun']
del liste66[3] # éliminer qqch
print(liste66)

    # .pop(indice)
liste688 = ['Francia', 'Alemania', 'Egipto', 'Camerun']
liste688.pop(3) # éliminer qqch. Attention ! il faut utiliser les ()
print(liste688)

    # liste.remove(text)
liste776 = ['Francia', 'Alemania', 'Egipto', 'Camerun']
liste776.remove("Francia") # C'est comme del mais ici je peux mentionner l'élément
print(liste776)

    # liste.clear()
liste7776 = ['Francia', 'Alemania', 'Egipto', 'Camerun']
liste7776.clear() # Élimine tous les éléments d'un liste
print(liste7776)




# IMPORT
    # random.randit(#,#)
import random 
variable_radom_entier = random.randint(0, 10) # Nombre entier random
print(variable_radom_entier) 

    # random.uniform
import random 
variable_radom_decimale = random.uniform(0, 20) # Nombre entier random
print(variable_radom_decimale) 

    # random.randrange
import random  
variable_range = random.randrange(10) # Nombre entier mais je n'ai pas besoin de mettre la limite en bas. ET le 10 n'est pas inclusive. 
print(variable_range)

    # range
liste98 = list(range(10)) # Attention ! pour avoir la liste de range, il faux utiliser le met list
print(liste98)

    # py_compile   .count("texte")
import py_compile
liste666 = ['Francia', 'Alemania', 'Egipto', 'Camerun', 'Alemania']
print(liste666.count("Alemania")) # nombre de fois que le mot allemagne apparaise

    # py_compile   .sort()
import py_compile
liste121 = ['Francia', 'Alemania', 'Egipto', 'Camerun', 'Alemania']
liste121.sort() # rangée de manière alpha ['Alemania', 'Alemania', 'Camerun', 'Egipto', 'Francia']
print(liste121)

    # py_compile   .reverse()
import py_compile
liste122 = ['Francia', 'Alemania', 'Egipto', 'Camerun', 'Alemania']
liste122.reverse() # inverser l'ordre de la liste ['Alemania', 'Alemania', 'Camerun', 'Egipto', 'Francia']
print(liste122)




# BOUCLES
# Les boucles nous permettent de parcourir des structures de données

    # for : il va executer plusieurs fois un code SANS une condition. 
for chaque_element_liste in [5, 8, 9, 10]:
    print(chaque_element_liste)

for chaque_element_list_1 in "Tout ce dont tu as besoin":
    print(chaque_element_list_1)

for elements_range in range(0,10):
    print(elements_range)

for elemets_range_1 in range(10,20):
    elemets_range_1 = elemets_range_1 + 1
    print(elemets_range_1)

for plusiers_mots in range(15):
    print("Bonjour")

liste89 = ["1", "2", "5", "Carlos", "8"]
for i in liste89:
    if i.isdigit() == True:
        print(i)  # 1  2  5  8     # Il va parcourir toute la liste


    # for continue : il nous permet d'alterer le déroulement d'un boucle.
liste89 = ["1", "2", "5", "Carlos", "8"]
for i in liste89:
    if i.isdigit() == True:
            continue
    print(i)  # Carlos


liste89 = ["1", "2", "5", "Carlos", "8"]
for i in liste89:
    if i.isdigit() == False:
        print(i) # Carlos


    # break    il va executer et ensuite caser la boucle
liste89 = ["1", "2", "5", "Carlos", "8"]
for i in liste89:
    if i.isdigit() == True:
        print(i)
        break  # 1


for i in liste89:
    if i.isdigit() == True:
        print(i)
    else:
        break # 1, 2, 5     Il va pas parcourrir toute la liste. Il arrête à partir du moment que c'est False



        # if and for
liste_de_nombre = [-1, -9, 0, 5, 8]
liste_de_nombre_positives = [(i*2) for i in liste_de_nombre if i >= 0]
print(liste_de_nombre_positives)



nombress = range(20)
numeros_modif_liste = [(i/2 if i <= 10 else i*2) for i in nombress]
print(numeros_modif_liste)


    #any and for
listepp = ['Francia', 'Alemania', 'Egipto', 'Camerun', '2' 'Alemania']
print(any([i.isdigit() == True for i in listepp]))


# page 101


























    # while : il va executer plusieurs fois un code AVEC des conditions. 
    # La condition doit être True. 

    i = 1
    while i <= 10:
        i+= 1 
        print(i)















