def lst_evennumber():
    lst = []
    for i in range(1,101):
        if i % 2 == 0:
            lst.append(i)
    return lst
print(lst_evennumber())