# keszits egy olyan programot amely megadott számok négyzetét számolja ki
# és ebből dictionary-t készít. pl: input: 3,
# output: {1: 1, 2: 4, 3: 9}

number = int(input('irj be egy szamot: '))
d = {}

# tól - ig: 'tól': inkluzív
# ig: exclusive
for i in range(1, number+1):
    d[i] = i*i
print(d)
