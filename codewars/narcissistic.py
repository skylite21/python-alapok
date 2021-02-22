def narcissistic(value):
    numbers = [int(char) for char in str(value)]
    power = len(numbers)
    summ = 0
    for number in numbers:
        summ = summ + number ** power
    if value == summ:
        return True
    return False

    # numbers = [int(char) for char in str(value)]
    # summ = sum([number ** len(numbers) for number in numbers])
    # return value == summ


print(narcissistic(371))
print(narcissistic(122))
