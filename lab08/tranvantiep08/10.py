def uoc_so(a): 
    lisst = []
    for i in range(1, a + 1): 
        if a % i == 0 : 
            lisst.append(i)
    return lisst

b = int(input('nhap mot so : '))
print(f'uoc so cua {b} la : ', uoc_so(b))