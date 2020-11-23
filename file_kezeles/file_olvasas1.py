file = open('./temp.txt', 'r')

print(file)

# lines = file.readlines()
print(file)
nums = []
for line in file:
    nums.append(int(line))

file.close()

print(nums)
