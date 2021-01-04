
# listak keszitese

# ez egy üres lista:
a = []
# string-eket tartalmazó szöveg
b = ['valami', 'szoveg']

# vegyes típusokat tartalmazó szöveg
c = ['valami', 42, True]
# listát listába is tehetünk.
d = ['kutya', [4, 3, 5], ['a']]
e = [[], [], [['a', 'b', 'c', ['x', 'y']]]]
# a b listából kiválasztja a második elemet
# a listákat nullától indexeljük
print(b[1])

print(c[2])

# listából listát kiválasztani:
print(d[2][0])
print(e[2][0][3][1])

# listához elemet az append-el hozzáadni mindig a lista legvégére!
a.append('szoveg1')
# az append függvényt a listán lehet meghívni
a.append('szoveg2')

print(a)

a = [2, 4, 6, 8, 10, 12, 14, 16, 18]

# ha tartományt választunk ki, akkor kettősponttal választjuk el
# tól:ig (ahol a felső korlát az exclusive)
# a tól: inclusive
print(a[2:5])
print(a[5:8])
print(a[1:7])
print(a[3:8])

# ha nem adunk alsó vagy felső korlátot:
print(a[2:])
print(a[:5])

print(a[:])  # = print(a)

# ha még egy kettőspontot beírunk akkor azt adjuk meg hogy
# hanyassával kérjük az elemeket
# PL :4-edik elemtől lefele mindet kérem, de kettessével
print(a[:4:2])

# megfordítja a listát:
print(a[::-1])

# megfordítja a listát és kettessével adja vissza az elemeket:
print(a[::-2])

# hátuólról is lehet elemet kiválasztani:
# pl legutolsó elem:
print(a[-1])


# ha egy pontos helyre akarjuk az elemet beilleszteni:
# pl: a 3-adik elem elé berakunk egy 'a' stringet
a.insert(3, 'a')
print(a)

# elemet kivenni a lista legvégéről
# ha kell, akkor a pop függvéy vissza is adja
# azt az elemet amit kitöröl
last = a.pop()
print(a)
print(last)

# ha adunk paramétert a pop-nak akkor az az
# index, azon az indexen lévő elemet kiveszi:
a.pop(1)
print(a)

# egy konkrét elemet kivenni (érték alapján)
a.remove('a')
print(a)

# ez errort dobna mert az elem már nincs benne a listában
# a.remove('a')

# hanyadik elem a 10-es:
print(a.index(10))

# megszámoljuk a 2-eseket a listában:
b = [2, 2, 4, 3, 2, 2, 2, 2]
print("{} darab kettes szám van a 'b' listában".format(b.count(2)))


# listák növekvő sorba rendezése:
c = [3, 7, 5, 12, 9]
c.sort()
print(c)

# string elemek esetén abc sorrendbe rendez
d = ['laci', 'bela', 'tibi', 'kati']
# ha a reverse flag-et True-ra állítjuk akkor fordított sorrendbe
# rendez:
d.sort(reverse=True)
print(d)

# megvofordítani a sorrendet:
a = [2, 4, 6, 8, 10, 12, 14, 16, 18]
a.reverse()
print(a)

x = ['h', 'e', 'l', 'l', 'o']
x.reverse()
print(x)

# kitörölni listából minden elemet:
x.clear()  # vagy:  x = []
print(x)

# listákat összefűzni:
a = [2, 4, 6, 8, 10, 12, 14, 16, 18]
x = ['h', 'e', 'l', 'l', 'o']
print(x + a)
# az a listát hozzáfűzzük az x listához:
x.extend(a)
print('A lista összefőzve metódussal: {}'.format(x))

a = [2, 4, 6, 8, 10, 12, 14, 16, 18]
x = ['h', 'e', 'l', 'l', 'o']
# zip: cipzár..
print(list(zip(x, a)))


s = 'this is my string'
# listává konvertálni:
my_string_list = list(s)
print(my_string_list)


# listát létrehozni stringből:
my_string_list = s.split(' ')
print(my_string_list)

s = '123-345-454'
my_string_list = s.split('-')
print(my_string_list)

# összeolvasztani listát stringgé:
# úgy hogy megmondjuk hogy mi legyen közötte
my_string = '*'.join(x)
print(my_string)
my_string = 'SZIA'.join(x)
print(my_string)
my_string = ''.join(x)
print(my_string)

# a join metódus csak olyan tömbökkel tud dolgozni
# ami string-eket tartalmaz
# my_string = '*'.join(a)    # << ERROR!

#                            👇🏻list comprehension!
my_string = '*'.join([str(item) for item in a])
print(my_string)

# list comprehension kifejtve for ciklussal:
result = []
for item in a:
    # result listába beletesszük az 'a' lista
    # minden elemét, stringgé alakítva:
    result.append(str(item))
# a result lista ugyanazt tartalmazza mint az 'a' lista
# csak int típusok helyett string-ek vannak benne:
print(result)
