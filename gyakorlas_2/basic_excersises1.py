# 1. készíts egy programot ami az alábbi tömbben eldönti
# az összes elemről hogy osztható e kettővel vagy nem
#
nums = [3, 4, 9, 6, 2]

# a kettővel oszthatóság ellenőrzését maradékos osztással
# kell megnézni:
# 8 % 2 == 0  # True mert a maradék nulla
# 3 % 2 == 0  # False mert van maradék

for num in nums:
    if num % 2 == 0:
        print("{}: osztható".format(num))
    else:
        print("{}: nem osztható".format(num))

# az eredményt így írd ki a képernyőre:
# 3: nem osztható
# 4: osztható
# 9: nem osztható
# 6: osztható
# 2: osztható


# 2. készíts egy programot ami kiirja a tömb összes elemét
# de úgy hogy az indexét is pl:
# ebből:
players = ['Peter', 'Kate', 'John']

# ezt írja ki:
# 0. Peter
# 1. Kate
# 3. John

for i, name in enumerate(players):
    print("{}. {}".format(i, name))


# 3. készíts egy fügvényt ami megvizsgálja egy elem
# összes tipusát, és kigyűjti őket egy tömbbe.
# pl ebből:
#
x = ['', 4, True]
# ezt csinálja:

['str', 'int', 'bool']

# Először hozz létre egy üres tömböt, és az append
# függvénnyel add hozzá a típusokat így:
# a = ['first']
# a.append['second']  # a is now: ['first', 'second']

types = []
for item in x:
    types.append(type(i).__name__)

print(types)
