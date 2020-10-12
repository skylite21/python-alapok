
health = 100
print(type(health))


def shoot():
    print('this arrow hits you')
    current_health = health - 10
    print('your health is {}'.format(current_health))


shoot()
