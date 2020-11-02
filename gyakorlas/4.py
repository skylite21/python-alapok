# készíts programot ami vesszővel elválasztott szavakat kér be
# és azokat rendezett listává alakítja

words = input('irj be szavakat vesszovel elvasztva: ')

print(words)

# a split metódus visszaadja a listát
words = words.split(',')

# a sort metódus a listán dolgozik
words.sort()

print(words)
