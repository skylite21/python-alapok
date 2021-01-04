

numbers = "2 4 7 8 10"
# numbers = "1 2 2"

numbers = numbers.split(' ')
print(numbers)

odds = []
evens = []
for number in numbers:
    number = int(number)
    if number % 2 == 0:
        evens.append(number)
    else:
        odds.append(number)

if len(odds) == 1:
    print(numbers.index(str(odds[0])) + 1)
else:
    print(numbers.index(str(evens[0])) + 1)
