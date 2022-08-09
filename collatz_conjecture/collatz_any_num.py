max_way = 0
number_collatz = 0


def collatz(arg):
    while arg > 0:
        yield arg
        arg -= 1


check_num = collatz(1_000_000)

for i in check_num:
    number = i
    score = 0
    while True:
        if i == 1:
            if score > max_way:
                max_way = score
                number_collatz = number
            break
        elif i % 2 == 0:
            i //= 2
            score += 1
        else:
            i = 3 * i + 1
            score += 1

print(f"The number - {number_collatz} max, "
      f"has a sequence of - {max_way} steps.")
