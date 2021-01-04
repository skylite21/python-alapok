# OOP : objektum orientált programozás
# ez egy programozási paradigma

player = ['John', 23, True, 54]

player1 = {'name': 'John', 'age': 23, 'alive': True, 'score': 54}

print(player1['name'])

player2 = {'name': 'John', 'age': 23, 'alive': True, 'score': 54}

# osztály deklarálása (általában nagybetűvel szoktuk)

# class-névnek a legjobb ha főnevet választunk...


class Animal:
    alive = True
    # osztályon belüli függvény:

    # __init__ metódus class-on belül: konstruktor fügvény
    # speciális függvény, minden példányosításnál automatikusan lefut
    def __init__(self, age, max_age):
        # self: speciális kulcsszó, a később létrejött objektum példányra utal
        # a self kulcsszó minden metódusnak az első paramétere kell hogy legyen
        self.age = age
        self.max_age = max_age
        print('Animal is initialized')

    # osztályon belüli függvény: metódosnak hívjuk (method)
    def eat(self):
        print("eating")

    def aging(self):
        self.age = self.age + 1
        if self.age >= self.max_age:
            self.alive = False

    def die(self):
        print('Animal is dead')
        self.alive = False


# osztály példányosítása: az a folyamat amely során
# létrejön az osztályból egy objektum példány
# Példányosításkor az osztály bemeneti paraméterei, az __init__ fgv bemeneti
# paraméterei...
my_animal = Animal(10, 50)
my_animal2 = Animal(50, 100)
print(my_animal2.age)
# a my_animal változó típusa: class (objektum példány)
print(type(my_animal))
print(my_animal.age)
my_animal.aging()
print(my_animal.age)
print(my_animal.alive)
my_animal.die()
print(my_animal.alive)

# üres osztály


class MyClass:
    pass

# öröklődés: a Dog osztály az Animal osztály
# minden tulajdonságát örökli


class Dog(Animal):
    name = ''

    def barking(self):
        print('{} is barking! Vau Vau!'.format(self.name))


class Cat(Animal):
    name = ''

    def meow(self):
        print('{} is meowing! meow meow!'.format(self.name))


my_dog = Dog(10, 15)
my_dog.name = 'Bodri'
print(my_dog.name)
my_dog.barking()
my_dog.aging()


# gorilla banana problem
class Chiwawa(Dog):
    height = 22
    # kettő aláhúzzással kezdődő property vagy metódus nevek:
    # pivate property: az objektum példány nem férhet hozzá
    __color = 'white'

    # a Dog osztály metódusát felülírjuk az alosztályban

    def barking(self):
        test = 'valami'
        print('Chiwawa! {}'.format(test))

    def get_color(self):
        print(self.__color)


my_chiwawa = Chiwawa(5, 15)
my_chiwawa.barking()
# my_chiwawa.__color # << erort dob!!

# csináltunk egy metódost ami hozzáfér a privát property-hez:
my_chiwawa.get_color()

# print(my_chiwawa.test) # <<< error!!

my_chiwawa.height = 100
print(my_chiwawa.height)
