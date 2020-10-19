

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

# 4. Megszámlálás tétele
# Számoljuk meg, hogy hány darab páros szám van a listában

db = 0
for elem in x:
    # oszthatóság vizsgálata maradékos osztás segítségével
    # ha nulla a maradék akkor a szám osztható 2-vel
    if elem % 2 == 0:
        db = db + 1

print("{} darab páros szám van a listában\n".format(db))

# 5. Maximum kiválasztás tétele

max_index = 0
for i, num in enumerate(x):
    if x[i] > x[max_index]:
        max_index = i

print("a legnagyobb elem a tömmben: {}".format(x[max_index]))

# 6. Buborékrendezés: rendezzük sorba az elemeket

n = len(x)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if x[j] > x[j + 1]:
            # kicseréljük a j-edik és a j+1-edik elemet:
            x[j], x[j+1] = x[j+1], x[j]

# a megrendezett x lista:
print(x)


# az x tömb elemeit újra összekeverjük a következő példához:
x = [5, 7, 2, 9, 5, 4]

# pythonban a lista rendezése
print(sorted(x))

# az x tömb elemeit újra összekeverjük a következő példához:
x = [5, 7, 2, 9, 5, 4]

# 7. Minimumkiválasztásos rendezés

for i in range(0, n):
    min_index = i
    for j in range(i+1, n):
        if x[min_index] > x[j]:
            min_index = j
    x[i], x[min_index] = x[min_index], x[i]

print(x)

# 8 Faktoriális számítása:


def fakt(n):
    if n == 0:
        return 1
    else:
        # rekurzív fügvény: saját magát meghívja
        return n * fakt(n - 1)


print(fakt(4))
