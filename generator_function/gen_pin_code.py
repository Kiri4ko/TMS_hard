from random import randint


def gen_pin(n_1):
    pin = [randint(0, 9)]
    while len(pin) != n_1 + 1:
        num = randint(0, 9)
        if num not in [pin[-1]]:
            pin.append(num)
            yield num


for i in gen_pin(4):
    print(i, end="")
