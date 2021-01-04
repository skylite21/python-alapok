

def digital_root(n):
    n = list(str(n))
    n = list(map(int, n))
    if len(n) == 1:
        print(n[0])
    else:
        digital_root(sum(n))


digital_root(16)
digital_root(132189)


# my_list = [3, 4, 5]
#
#
# def times2(x):
#     return x*2
#
#
# print(times2(3))
#
# my_new_list = []
# for num in my_list:
#     my_new_list.append(times2(num))
#
# my_new_list = list(map(times2, my_list))
# print(my_new_list)
