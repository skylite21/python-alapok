class A():
    def __init__(self):
        print('A')

    def foo(self):
        print('foo')


class B():
    def __init__(self):
        print('B')

    def bar(self):
        print('bar')


# a C osztály először az A osztály metóodusait örökli, majd a B-ét
# Az A osztály init metódusa van előrébb, tehát az lesz az érvényes, nem a B
# osztály init metódusa...
class C(A, B):
    def foobar(self):
        self.foo()
        self.bar()


c = C()
c.foobar()
print(C.__mro__)
