# 1. feladat: keszits prograomt ami egy neveket tartalmazó listában
# megmondja hogy van e benne Pista es kiirja azt is hogy hanyadik elem
# a listában a Pista
#

names = ['Gabor', 'Gábor', 'István', 'István',
         'László', 'Katalin', 'Katalin', 'Tímea', 'Gábor', 'Pista']

try:
    van_pista = names.index('Pista')
    print('Pista ezen a helyen van: {}'.format(van_pista))
except ValueError:
    print('Nincs Pista!')

# 2. feladat: keszits programot ami egy szamokat tartalmazo tomb-on vegig megy
# es egy osszeg valtozoba bepakolja a szamok osszegét. A ciklus után az osszeg
# valtozot irja ki a kepernyore

nums = [2, 4, 5]
sum_of_nums = 0
for num in nums:
    sum_of_nums = sum_of_nums + num

print(sum_of_nums)

#
# 3. Az elozo programot bovitsd ki úgy hogy uzenetet dobjon ha a tomb
# egyik eleme
# nem szam, es azt ne vegye figyelembe, de igy is osszegezze a többi number
# tipusu elemeket, es irja ki az eredmenyt

nums = [2, 4, 's', 5]
sum_of_nums = 0
for num in nums:
    if type(num) is int:
        sum_of_nums = sum_of_nums + num

print(sum_of_nums)
#
# 4. Az elozo programot bovitsd ki ugy hogy amennyiben nem szam a tomb
# egyik eleme
# akkor probalja meg a program a int fgv-el atkonvertalni
# számmá, és ezután
# újra nézze meg hogy szám e az adott elem. Ha igen, adja hozzá,
# ha nem, jelezze
# egy print-el hogy nem sikerult a konvertalas annál az elemnél
#

nums = [2, 4, '4', 5, 's']
sum_of_nums = 0
for num in nums:
    try:
        num = int(num)
    except ValueError:
        print('nem sikerult a konvertalas')
    if type(num) is int:
        sum_of_nums = sum_of_nums + num

print(sum_of_nums)
