
# a tuple ugyanúgy elemeket tartalmaz mint a lista
my_tuple = (4, 'szoveg', True, [])

print(my_tuple)
# elemeket kiválasztani uganúgy lehet mint a listánál...
print(my_tuple[1])

# a tuple elemin nem lehet módosítai, újat hozzáadni, elvenni..stb..
# my_tuple.append(0) # <<< ERROR

# a tuple csak olvasható
# my_tuple[1] = 'e' # <<< ERROR

#  át tudjuk alakítani a tuple-t listává:
my_list = list(my_tuple)
print(my_list)
