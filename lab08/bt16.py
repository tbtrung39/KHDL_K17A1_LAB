def day_so_chan():
    list = []
    for i in range(1,101):
        if i % 2 == 0:
            list.append(i)
    return list
print("Dãy số chẵn thuộc khoảng [1,100]:",day_so_chan())