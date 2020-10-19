

# Csere algoritmus

a = 5
b = 9
# cseréljük ki a és b változó értékét, egy segédváltozóval
c = a
a = b
b = c

print(a, b)

# pythonos megodása a cserének:

a, b = b, a
print(a, b)


# 1. sorozatszámítás tétele
x = [5, 7, 2, 9, 5, 4]
osszeg = 0
for elem in x:
    osszeg = elem + osszeg

print(osszeg)

# pythonos megoldás:
print(sum(x))

# 2. eldötés tétele
# döntsük el hogy van e a listában 2-es szám
# n = a tömb elemeinek száma
n = len(x)
i = 0
while i < n and x[i] != 2:
    i = i + 1
if i < n:
    print('van benne 2-es')
else:
    print('nincs benne 2-es')


# pythonban ha meg akarjuk nézni hogy egy adott elem
# létezik e a tömbben:

print(2 in x)

# 3. Lineáris keresés tétele
# lényegében ugyanaz mint az eldöntés, csak ez az indexet
# adja vissza (hanyadik elem a 2-es szám...)
n = len(x)
i = 0
while i < n and x[i] != 2:
    i = i + 1
if i < n:
    print('van benne 2-es, ezen az indexen: {}'.format(i))
else:
    print('nincs benne 2-es')

# pythonban ha indexet keresünk:
# hanyadik elem a 2-es szám:
print(x.index(2))
