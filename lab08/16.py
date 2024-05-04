def bai16():
    lst = []
    for i in range(1,101):
        if i % 2 == 0:
            lst.append(i)
    return lst
    
print(bai16())