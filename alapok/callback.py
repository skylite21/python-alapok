a = [1, 2, 4]


def get_square(n):
    return n**2


b = []
for e in a:
    b.append(get_square(e))

print(b)

# callback: egy olyan függvény ami egy másik függvény bemeneti paramétereként
# szerepel

print(list(map(get_square, a)))
