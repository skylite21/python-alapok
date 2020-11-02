# irj egy programot ami egy számokat tartalmazó tömbből, kiveszi a duplikáltakat
# és csak az egyedi elemeket adja vissza
# pl. 3,3,4,5,5 -> 3,4,5

num_list = input('irjon be szamokat vesszővel elvasztva: ')

num_list = num_list.split(',')
uniq_num_list = []

for num in num_list:
    if num not in uniq_num_list:
        uniq_num_list.append(num)

print(', '.join(uniq_num_list))
