
# a set ugy néz ki mint a dict csak nincsenek value-k...
my_set = {3, 5, 6}
print(my_set)
print(type(my_set))

my_set.add(4)
my_set.add(3)
my_set.add(3)
my_set.add(3)
my_set.add(3)
print(my_set)
my_set = {'asd', 4, 10, True}
print(my_set)
my_set.add(True)
print(my_set)

# kiszedjük egy listából a duplikált elemeket:
my_list = [1, 1, 3, 3, 3, 4, 5]
my_uniq_list = list(set(my_list))
print(my_uniq_list)
