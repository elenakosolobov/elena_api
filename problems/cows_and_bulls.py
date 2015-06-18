from random import randint


def generate_random_list():
    return [randint(0, 9) for x in range(4)]


def user_input():
    l = []
    while not l:
        try:
            x = raw_input('\nEnter 4 digit number: ')
            if len(x) == 4:
                l = [int(y) for y in str(x)]
            else:
                print('Wrong Input')
        except ValueError:
            print('Wrong Input')
    return l


def count(l1, l2):
    cows = 0
    bulls = 0
    for i in range(4):
        if l1[i] == l2[i]:
            bulls += 1
            l1[i] = None
            l2[i] = None
    for i in l1:
        for y in l2:
            if i == y and i and y:
                cows += 1
    return cows, bulls

print('Cows: %s, Bulls: %s' % count(user_input(), generate_random_list()))