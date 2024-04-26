def so_chan():
    lst = list(map(lambda i: i, filter(lambda i: i % 2 == 0, range(1, 100+1))))
    return lst

print(so_chan())