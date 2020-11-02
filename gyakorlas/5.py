#  készíts programot ami egy bevitt mondatban megszámolja a számokat és a betűket (külön)
#  és kiírja az eredményt. pl: szia 123     -> betűk: 4, számok: 3

sentence = input('irj be egy mondatot: ')
digits = 0
letters = 0
for c in sentence:
    if c.isdigit():
        digits = digits + 1
    if c.isalpha():
        letters = letters + 1

print("betűk száma: {}, számok száma: {}".format(letters, digits))
