# alakítsd át list comprehention-re az alábbi ciklusokat:
# new_list = [expression for member in iterable]

nums = [2, 5, 9, 6]
nums_new = []
for num in nums:
    if num % 2 == 0:
        nums_new.append(num)

print(nums_new)
# for list comprehensions with if conditions only,
# [f(x) for x in sequence if condition]
nums_new = [num for num in nums if num % 2 == 0]

print(nums_new)

strings = ['a', '', 'b', 'c']

new_strings = ['' if string == 'a' else string for string in strings]
print(new_strings)
