def so_chan():
    list = []
    for i in range(1,101):
        if i % 2 == 0:
            list.append(i)
    return list
print(so_chan())