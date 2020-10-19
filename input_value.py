
def jatek():
    num = input("Irj be egy szamot: ")

    try:
        test_num = int(num)
        test_num = test_num + 1
        print('\n {}, én nyertem'.format(test_num))
    except ValueError:
        print('ez nem szám')

# jatek()


nums = input('Irj be számokat vesszővel elválasztva!\n')
# itt a nums valtozo még string
print(nums)
# a strip fügvény leszedi a string elejéről és a végéről
# a megadott karaktert/karaktereket (jelen esetben a vesszőt)
nums = nums.strip(',')
print(nums)
# a split fügvény a stringekből listát csinál, a vessző kakater
# lesz a delimiter (elválasztó)
# a nums változó mostantól nem string tipusú hanem lista!
nums = nums.split(',')
print(nums)

# keressük meg a listában lévő legnagyobb értéket! (maximum)
# itt nincs hibakezelés!
max_index = 0
for i, num in enumerate(nums):
    if int(nums[i]) > int(nums[max_index]):
        max_index = i

print('a legnagyobb elem: {}'.format(nums[max_index]))
print('a legnagyobb elem helye: {}'.format(max_index))
