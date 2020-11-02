# készíts egy programot ami az alábbi mintát rajzolja ki:
# pl: input: 4
# 1
# 2 2
# 3 3 3
# 4 4 4 4

num = int(input("irj be egy számot: "))

for i in range(1, num+1):
    for j in range(1, i+1):
        if j == i:
            print(i, end='')
        else:
            print(i, end=' ')
    print('')
