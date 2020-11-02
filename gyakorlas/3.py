# készíts programot ami kettő számot kér be és abból egy két dimenziós listát csinál
# pl: 2,3     ->   [[0,1,2], [0,1,2]]

outer_list_length = int(input('ird be az elso szamot: '))
inner_list_length = int(input('ird be a masodik szamot: '))

nums = []
inner_nums = []

for num in range(0, inner_list_length):
    inner_nums.append(num)

for num in range(0, outer_list_length):
    nums.append(inner_nums)

print(nums)
