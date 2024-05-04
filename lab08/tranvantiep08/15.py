def make_list(n) : 
    lisst = []
    for i in range(n) :
        num = int(input(f'nhap so nguyen thu {i + 1} la : '))
        lisst.append(num)
    return lisst

c = int(input('so luong phan tu la : '))
list_moi = list(filter(lambda x: x % 2 != 0, make_list(c)))
lisst_moi = list(map(lambda x: x ** 2, list_moi))
print(lisst_moi)