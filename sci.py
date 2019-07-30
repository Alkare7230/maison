#coding:utf-8

# un commentaire d'une seul ligne
"""
Roh kjfldsklsdk

Nommer uen variable: doit commencer par une lettre ou un underscore
                     ne doit pas contenir de caractère spéciaux
                     ne pas contenir d'espaces
                     utiliser des underscore (_)

Type standards : entier numérique (int)
                 nombre floattant (float)
                 chaîne de caractère (str)
                 Booléen (bool)
                 Autre (Liste, dictionnaire, tuple, ect.)

Fonction         Print()      -> afficher à l'écran
                 Type()       -> retourne le type d'une Fonction
                 input()      -> lire au clavier/ ajouter une donner via l'inviter de commande
                 str.format() -> chaîne de caractère avec le quel on peut lier des fonction dans
                 print ou autre.
                 int(), float(affiche les nombre à virgule), str(), bool(), -> "Caster" une donnée, la convertir.

Opérateurs en Python : + (addition)
                       - (soustration)
                       * (multiplication)
                       / (division)
                       % (modulo) -> reste d'une division Euclidienne
                       (Pour simplier les nombre avec des decimal vous pouvez utilisez 5.0 /2.0 (au lieux du float pour retourner le resultat))
Variable = Variable + x
Variable += x

Variable -= x
Variable = Variable - x

Variable *= X
Variable = varible * x

Opérateur de comparaison : == (égale à)
                           != (Diférent de)
                           < (plus petit que)
                           > (plus grand que)
                           <= (plus petit ou égale à)
                           >= (plus grand ou égale à)


Condition multiple :       and (ET)
                           or(OU)
                           in / not in (DANS / PAS DANS)


mots clés : if / elif / else


age > 0 ET age <= 100 --> 0 < age <= 100

i = i + i
i += 1

Boucle : While / for
Mots clés : break/ continue

Importer un module : import <nom_du_module>
                     from <nom_du_module> import <nom_fonction>
                     from <nom_du_module> import *



Gérer les exceptions : Try/except (+ else, finally)

Type exception : ValuesError
                 ZeroDivisionError
                 OSError
                 AssertionError


Classe des être humains :
"""
#___________________________________________________________________________
import faker

fake = faker.create()

fake.name()

fake.address()
fake.text()

print(fake.name())




#__________________________________________________________________________________
