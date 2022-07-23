from random import randint

num_game = randint(0, 10)
game = (int(input("Your number - ")) for i in range(4))
for i in game:
    if i == num_game:
        print("Right! You win!!!")
        break
    elif abs(i - num_game) == 1:
        print("Warm!")
    else:
        print("Cold")
print("Game over!")
