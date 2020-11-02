# -*- coding: utf-8 -*-
# készíts egy programot ami addig irja ki a beírt számok összegét amíg a user
# be nem ír egy negatív számot

sum_of_nums = 0
while True:
    num = int(input('irj egy szamot: '))
    if num < 0:
        break
    sum_of_nums = sum_of_nums + num
    print(sum_of_nums)
