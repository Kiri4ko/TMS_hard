from random import randint

pin = (randint(0, 9) for i in range(4))
for i in pin:
    print(i, end=" ")
