
nums = []

# a with kulcsszóval nem kell close-olni a file-t
# a blokk végén automatikusan bezárul a file
with open('./temp.txt', 'r') as file:
    for line in file:
        nums.append(int(line))

print(nums)
