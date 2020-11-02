# irj egy proramot ami bekér vesszővel elválasztott számokat
# és azokból egy listát generál

nums = input('irj be számokat: ')

lista = nums.split(',')
# lista.append('uj elem')
print(lista)

# tuple: nem módosítható lista
my_tuple = tuple(lista)
print(my_tuple)
