

# alapértelmezetten ha nincs szülője egy osztálynak
# akkor az alapértelmezett szülője az object
class Pet(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # getter: olyan metódus ami visszadja az objektum egy paraméterét
    def get_name(self):
        return self.name

    # setter: olyan metódus ami módosítja az objektum egy paraméterét
    def set_name(self, new_name):
        print('name changed...')
        self.name = new_name
    # az __str__ metódus arra való hogy stringként megjelenítsük az objektum
    # nevét
    # __ double underscore = dunderscore

    def __str__(self):
        return "{} is a {}".format(self.name, self.species)


class Dog(Pet):
    # overloading: a szülő osztály már rendelkezik __init__-el de
    # ez itt most módosul...
    def __init__(self, name, chase_cats=False):
        # super fgv: a szülő osztályt hívja meg
        # a következő sor a Pet osztály konstruktor-át hívja meg
        super().__init__(name, 'dog')
        self.chase_cats = chase_cats

    def is_chasing_cats(self):
        return self.chase_cats

    # overwriting: egy metódus teljes felülírása a szülőhöz képest...
    def __str__(self):
        additional_info = ''
        if self.chase_cats:
            additional_info = " who chases cats"
        return super().__str__() + additional_info


p = Pet('Polly', 'parrot')
p.set_name('Peter')
print(p.name)
print(type(p))
print('{} is a {}'.format(p.name, p.species))
print(p.__str__())


d = Dog('Fred', True)
print(d.__str__())
print(d.is_chasing_cats())

# visszaadja az osztály szülő osztályát (osztályait...)
print(Dog.__bases__)
# egy osztály összes gyerek osztályát adja vissza:
print(Pet.__subclasses__())

# milyen sorrendben próbálja megkeresni a python a metódusokat és property-ket
# az adott osztályon
print(Dog.__mro__)
