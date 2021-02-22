# 1. készíts egy programot ami egy 5x5ös mátrix minden elemét összegzi. pl:

m = [[1, 1, 1, 2, 1], [2, 3, 2, 2, 2], [3, 3, 2, 3, 3], [4, 4, 4, 3, 4]]

# az eredmény: 50

# 2. Készíts programot ami az alábbi autókat tartalmazó tömböt megvizsgálja és
# kiírja azoknak az autóknak a típusát amelyeknél az utasok száma túl nagy
cars = [
    {"price": 1549,
     "passengerQty": 4,
     "currency": "EUR",
     "type": "Kia",
     "transmission": "manual",
     "passengers": [
         "Gabor",
         "Andras",
         "Timea",
         "Martin",
         "Miklos"
     ]
     },
    {"price": 1954,
     "passengerQty": 5,
     "currency": "EUR",
     "type": "Suzuki",
     "transmission": "manual",
     "passengers": [
         "Gabor",
         "Andras",
         "Timea",
         "Martin",
         "Miklos"
     ]
     },
    {"price": 2544,
     "passengerQty": 5,
     "currency": "USD",
     "type": "Opel",
     "transmission": "manual",
     "passengers": [
         "Gabor",
         "Andras",
         "Timea",
         "Martin",
         "Miklos"
     ]
     },
    {"price": 2544,
     "passengerQty": 2,
     "currency": "USD",
     "type": "Opel",
     "transmission": "manual",
     "passengers": [
         "Gabor",
         "Timea",
         "Miklos"
     ]
     },
    {"price": 9542,
     "passengerQty": 4,
     "currency": "USD",
     "type": "Ford",
     "transmission": "automatic",
     "passengers": [
         "Gabor",
         "Timea",
         "Miklos"
     ]
     },
]

# pl kimenet:

# a(z) Kia típusú autóban túl sok az utas
# a(z) Opel típusú autóban túl sok az utas

# 3. az előző cars tömbben váltsd át az autók árát euróból usd-be, és listázd
# ki az eredményt de csak az autó neve és ára legyen kiírva (és a pénznem)
# figyelj rá hogy átváltáskor nem csak a price-ot kell módosítani hanem a
# currency-t is

# 4. az alábbi kettő tömbből készítsd el a lenti kimenetet:
persons = ["John", "Marissa", "Pete", "Dayton"]
restaurants = ["Japanese", "American", "Mexican", "French"]

# John eats Japanese
# John eats American
# John eats Mexican
# John eats French
# Marissa eats Japanese
# Marissa eats American
# Marissa eats Mexican
# Marissa eats French
# .... a többi névre is

# 5.
# alakítsd át az alábbi tömböt úgy, hogy minden belső
# listaába egy harmadik elemet raksz, ami az előző
# kettő szám összegét tárolja
my_list = [[4, 5], [7, 4], [2, 5], [9, 4]]
# eredmény:  [[4, 5, 9], [7, 4, 11], [2, 5, 7], [9, 4, 13]]
