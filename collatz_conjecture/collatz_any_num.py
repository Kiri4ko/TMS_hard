data = []
for i in range(1, 1000000001):
    lst = [i]
    while True:
        if i == 1:
            lst[:] = lst[0], len(lst) - 1
            data.append(lst)
            if data[0][1] <= lst[-1]:
                data.clear()
                data.append(lst)
            else:
                data.remove(data[-1])
            break
        elif i % 2 == 0:
            i //= 2
            lst.append(i)
        else:
            i = 3 * i + 1
            lst.append(i)
print(f"The number - {data[0][0]} max, "
      f"has a sequence of - {data[0][1]} steps.")
