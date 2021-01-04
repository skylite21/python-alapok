
# ha csak egy két függvényre van szükség:
# from my_module import say_hi, multiply
# az egész modult beimportálja:
import my_module

# ha az egész modult importáltuk akkor így kell rá hivatkozni:
my_module.say_hi()
my_module.multiply(4, 4)

# ha csak a függvényeket importáltuk be akkor egyszerűen meghívhatók:
# say_hi()
# multiply(5, 6)
