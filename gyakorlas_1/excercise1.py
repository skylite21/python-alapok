# Python feladatok
#
#
# Feladat
#
# Készíts egy programot ami megtalál minden számot 2000 és 3200 között ami
# osztható 7-el, de nem osztható 5-el.

import math
oszthatok = []
for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        oszthatok.append(num)

print(oszthatok)

#
# Segítség: használd a range függvény-t és az append-et
#
#
# Feladat
# Adott az alábbi tömb:
#
names = ['Pista', 'Gabor', 'Pista', 'Gábor', 'István', 'István',
         'László', 'Katalin', 'Katalin', 'Tímea', 'Gábor', 'Pista']


# Készíts egy programot ami megszámolja ebben a tömbben a Pistákat

pista_cont = 0
for name in names:
    if name == 'Pista':
        pista_cont += 1

print(pista_cont)

# rövidebb megoldás:
print(names.count('Pista'))


# Feladat
# Kérj be a felhasználótól egy számot az input függvény segítségével. Ez után
# próbáld meg a számot int függvényyel számmá alakítani, végül készíts egy
# ciklust ami annyiszor fut le amekkora számot beírt a felhasználó, és
# annyiszor írja ki a képernyőre hogy Helló, de a sorokat is számozza (1től)!


num = input("irj be egy szamot: ")

try:
    test_num = int(num)
    for i in range(test_num):
        print("{}: Helló".format(i+1))
except ValueError:
    print('ez nem szam')


# Feladat
# Készíts egy programot ami bekér a felhasználótól egy számot, amit az int
# függvénnyel alakíts számmá. A bekért szám egy kör sugara legyen, a program
# pedig számolja ki a kör sugarából a kör területét és kerületét. A számításhoz
# használd ezt a képletet https://www.calculat.org/hu/terulet-kerulet/kor.html
#

num = input("irj be egy szamot: ")

try:
    r = int(num)
    print('a kör kerülete: {}'.format(2*r*math.pi))
    print('a kör területe: {}'.format(r*r*math.pi))
except ValueError:
    print('ez nem szam')
#
# Feladat
# Adott az alábbi tömb:

names = ['Gaál Bernadett', 'Szamosi Judit', 'Tóth Sára',
         'Magyar Eszter', 'Gaál András', 'Németh Diána',
         'Telek Éva', 'Ledán-Munteán Szabolcs',
         'Mészáros Melinda', 'Lukács Dániel', 'Kucsera Bálint', 'Kovács Tamás']

# Készíts
# programot ami a neveket abc sorrendbe rendezi (sorted függvénnyel) majd a
# csoportot két részre osztja (megfelezi) és kiírja a képernyőre a két
# csoportot külön. Például így:

# csoport:
# Gaál András
# Gaál Bernadett
# Kovács Tamás
# Kucsera Bálint
# Ledán-Munteán Szabolcs
# Lukács Dániel
# csoport:
# Magyar Eszter
# Mészáros Melinda
# Németh Diána
# Szamosi Judit
# Telek Éva
# Tóth Sára
#
#
# Bővítsd a programot arra az esetre ha a nevek száma páratlan!
#

sorted_names = sorted(names)
if len(sorted_names) % 2 == 0:
    half_index = int(len(sorted_names)/2)
    group1 = sorted_names[:half_index]
    group2 = sorted_names[half_index:]

print('1. csoport:')
for name in group1:
    print(name)

print('2. csoport:')
for name in group2:
    print(name)
