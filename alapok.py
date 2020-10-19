# meghívjuk a print füvgényt és átatjuk neki a
# 'hello world' stringet
# a kettőskeressztel kezdődő sorokat a python nem értelmezi
# a kettőskeressztel kezdődő sorok comment-ek]

print('hello world')
# létrehoztunk egy szoveg nevű változót, az értéke pedig a
# 'sziasztok!' karakterlánc
# ha egy darab egyenlőségjelet látunk a kódban az minden esetben
# értékadást jelent. Az egyenlőségjel jobb oldala bekerül az
# egyenlőségjel bal oldalán lévő változóba.
szoveg = 'sziasztok!'
print(szoveg)
# szekvencia: a program az utasításokat (sorokat) soronként
# hajtja végre egymás után
# a következő sor hibát dobna, mert nem hoztuk még létre a szoveg2
# változót:
# print(szoveg2)
szoveg2 = "alma"
# meghívjuk a format fgv-t az aposztrofok közötti szövegre
print('a szoveg2 értéke: {}'.format(szoveg2))
# megnézzük a szöveg2 változó típusát:
print(type(szoveg2))

# ha valahol látunk egy sima zárójelet és előtte valami szöveget
# pl.:   sdfsdfsdf()
# ez egy fügvényhívást jelent, a füvény neve a
# nyitó zárójel előtti rész

# python autocomplete funkció, help ablakkal!!
# autocomplete = intellisence = code complete

print('a szoveg erteke: {} a szoveg2 erteke {}'.format(szoveg, szoveg2))
# létrehozzuk a szam nevű változót és az érték amit kap ez a változó
# az egy szám lesz (nincs körülötte aposztrof, vagy idézőjel)
# dinamically typed programming language: a változók típusát
# létrehozáskor (deklaráláskor) automatikusan megpróbálja kitalálni
# a futtató környezet (python)
szam = 34
print(type(szam))
szam1 = 10
print(szam+szam1)

# növeljük egyel a szám változó értékét
szam = szam + 1
# az elző sor rövidebben:
szam += 1
print(szam)

# string = szoveg
# int (integer) = szám

# boolean tipusú változó, két érteke lehet: True vagy False
kapcsolo = True
print(type(kapcsolo))

# elágazás egy olyan kód blokk ami egy adott feltétel alapján
# vagy lefut vagy nem...

if kapcsolo is True:
    print('A kapcsoló fel van kapcsolva')

print('ez már az if blokkon kívül van...')

a = 3
b = 4

if a > b:
    print('az a nagyobb mint b')
else:
    print('a nem nagyobb mint b')


# ciklus: egy adott kódrész többször fut le
# egy adott feltétel szerint

szam = 10
while szam > 0:
    print('a szám változóból levonunk 1-et: {}'.format(szam))
    # szam = szam - 1
    szam -= 1

# a kapcsos zárójel a python-ban a lista típusú változót jelenti
# a kapcsos zárójelen belűlre írjuk a lista elemeit
# a listába több elemet is el lehet tárolni
# más programozási nyelvek ezt tömb-nek hívják
nevsor = ['Pista', 'Kata', 'Tibor']

# a for ciklust legtöbbször arra használjuk hogy
# végig menjünk egy lista összes elemén és az elemeken
# valamilyen műveletet végezzünk:
for nev in nevsor:
    print('a névsorban szerepel: {} '.format(nev))

# pythonban a lista elemeit nullától indexeljük
for index, nev in enumerate(nevsor):
    print('{} :  {} '.format(index+1, nev))

print('a nevsor nulladik eleme: {} '.format(nevsor[0]))


def divisible_by_three(num):
    if type(num) != int:
        # return None
        return 'nem szamot kaptam'

    if num % 3 == 0:
        # early return
        return True
    return False


print(divisible_by_three(9))
print(divisible_by_three(4))
print(divisible_by_three('4'))


def divisible_by_three_better(num):
    # a try - except blokk hiba kezelésre használható
    # ha a try blokkban lévő kód ValueError-t dob akkor az
    # except ValueError-ban lévő rész fog lefutni.
    try:
        num = int(num)
        if num % 3 == 0:
            # early return
            return True
        return False
    except ValueError:
        return 'nem szamot kaptam'


print(divisible_by_three_better('4'))
print(divisible_by_three_better('sadsdf'))

# 0-tól 4ig megy
for i in range(5):
    # az end paraméter a string végére beteszi amit aposztrof-ok közé írtunk
    print(i, end=', ')

print('\n')
# 5től 9-ig:
for i in range(5, 10):
    print(i, end=', ')

print('\n')
# 5től 25ig 2-essével:
for i in range(5, 25, 2):
    print(i, end=', ')
