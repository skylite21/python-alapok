import time


def timing_function(callback):
    def wrapper():
        t1 = time.time()
        callback()
        t2 = time.time()
        print(" time it took to run the function: {}".format(t2-t1))

    # egy új függvényt ad vissza a timing_function
    return wrapper


def my_function():
    num_list = []
    for num in range(0, 10000):
        num_list.append(num)
    print("sum of all numbers: {}".format(sum(num_list)))


my_function_timed = timing_function(my_function)
my_function_timed()

# decorator: a my_function függvény úgy jön létre, hogy a timing_function-ben
# callback-ként lefut...


@timing_function
def my_function():
    num_list = []
    for num in range(0, 10000):
        num_list.append(num)
    print("sum of all numbers: {}".format(sum(num_list)))


my_function()
