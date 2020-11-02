# irj egy programot ami az alábbi mintát rajzolja ki:
# pl.> input: 4
# * * * *
# * * *
# * *
# *

num = int(input('irj be egy számot: '))

for i in range(num, 0, -1):
    for j in range(0, i):
        print('* ', end='')
    print('')
