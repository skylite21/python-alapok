num_list = []

with open('temp.txt', 'r') as file:
    for line in file:
        num_list.append(int(line))
print(num_list)
