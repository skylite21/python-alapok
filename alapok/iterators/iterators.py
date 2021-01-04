
# tuple, list, set, dict... = iterable
# az iterable egy olyan objektum amiből lehet iteratort csinálni
my_list = [1, 2, 3]


# iterator: egy olyan object aminek van __next__ methodja
iter = my_list.__iter__()
print(iter)
print(type(iter))
print(iter.__next__())
print(iter.__next__())
print(iter.__next__())

# list comprehention

numbers = [1, 2, 3, 4]
# numbers_again = numbers
numbers_again = [n for n in numbers]
print(numbers_again)
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)
odd_numbers = [n for n in numbers if n % 2 == 1]
print(odd_numbers)
odd_squares = [n**2 for n in numbers if n % 2 == 1]
print(odd_squares)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [e for row in matrix for e in row]
print(flat)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = []
for row in matrix:
    s = ''
    for elem in row:
        s = s+str(elem)
    flat.append(s)
print(flat)
