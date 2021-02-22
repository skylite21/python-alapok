
class Counter:
    def __init__(self, value):
        self.value = value
        self.step = 1

    def increment(self):
        self.value += self.step

    def decrement(self):
        self.value -= self.step

    def set_value(self, val):
        self.value = val

    def set_step(self, step):
        self.step = step

    def get_value(self):
        print(self.value)

    def get_step(self):
        print(self.step)


class ScoreCounter(Counter):
    def __init__(self, value, name, age):
        self.value = value
        self.name = name
        self.age = age
        self.step = 1
        self.winner = False

    def increment(self):
        self.value += self.step
        if self.value >= 12:
            self.winner = True


myScoreCounter = ScoreCounter(10, 'Zsolt', 34)
myScoreCounter.increment()
myScoreCounter.get_value()
myScoreCounter.increment()
# myScoreCounter.get_value()
print(myScoreCounter.winner)
