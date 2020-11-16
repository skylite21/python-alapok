
# egy üres dictionary:
my_dict = {}

my_dict['my_key'] = 43

# a dictionary olyan mint a lista, több elem lehet benne, de
# az elemeknek van cimkéje is.
print(my_dict)

my_dict = {'pista': '123-123-123', 'kati': '345-345-345'}
# my_test_dict = {2: 'pista'}
# print(my_test_dict[2])

print(my_dict['pista'])

my_dict = {'people': ['pista', 'geza', 'tibi'],
           'x': {'a': 'value of a', 'b': [1, 2, 3]}}

print(my_dict['x']['b'][0])
print(my_dict['people'][1])
print(my_dict["people"][1])
print(type(my_dict))

# print(my_dict{'people'}) <<< ERROR!

# a get metódus szintén key alapján valute-t ad vissza
print(my_dict.get('people')[0])

# a kettőspont bal oldalán van a key, a jobb oldalán a value
my_dict = {'myKey': 'value'}

print(my_dict.get('asd'))  # <<< None-t ad ha nem létezik
# print(my_dict['asdasd'])  # <<< ERROR ha nem létezik

# ha nem létezik az adott key akkor létrehozza a key-t és a value-t
# ha létezne már ez a key, akkor új értket kapna
my_dict['myNewKey'] = True
print(my_dict)


# pop metódust használhatjuk elemek törlésére (key alapján)
my_dict.pop('myNewKey')
print(my_dict)

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

# copy: másolatot csinál a dictionary-ről
# mert iteráció közben nem módosíthatjuk az
# annak a dictionary-nek az elemeit
# amin végig loop-olunk
for key, value in my_dict.copy().items():
    if value == 3:
        my_dict.pop(key)

print(my_dict)


# dictionary egybeolvasztás
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
my_dict2 = {'e': 1, 'f': 2, 'c': 6, 'g': 4}

my_dict.update(my_dict2)
print(my_dict)

# a key az egyedi, és csak egy lehet belőle
my_dict['e'] = 3


# dictionary készítés listákból
l1 = ['a', 'b', 'c']
l2 = [1, 2, 3]
my_dict = dict(zip(l1, l2))
print(my_dict)

l3 = [('a', 1), ('b', 2)]
print(dict(l3))
