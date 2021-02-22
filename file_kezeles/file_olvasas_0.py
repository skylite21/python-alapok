file = open('temp.txt')

num_list = []

# lines = file.readlines()
for line in file:
    num_list.append(int(line))

file.close()

print(num_list)
