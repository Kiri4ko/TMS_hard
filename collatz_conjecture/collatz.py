data = []
for i in range(1, 28):
    lst = [i]
    while True:
        if i == 1:
            lst[:] = lst[0], len(lst) - 1
            data.append(lst)
            break
        elif i % 2 == 0:
            i //= 2
            lst.append(i)
        else:
            i = 3 * i + 1
            lst.append(i)
max_date = max(data, key=lambda data: data[1])
print(f"The number - {max_date[0]} max, "
      f"has a sequence of - {max_date[1]} steps.")
