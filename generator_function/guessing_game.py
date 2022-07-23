from random import randint


def guessing_game(num_att, ran_1, ran_2):
    num = randint(ran_1, ran_2)
    print(
        f"Guess a number from {ran_1} to {ran_2}.",
        f"You have {num_att} attempts."
    )
    for i in range(num_att):
        user_num = int(input("Your number - "))
        if num == user_num:
            yield "Right! You win!!!"
            break
        elif abs(num - user_num) == 1:
            yield "Warm!"
        else:
            yield "Cold"
    yield "Game over!"


for i in guessing_game(3, 0, 10):
    print(i)
