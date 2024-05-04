def make_list(n) : 
    lisst = []
    for i in range(n) :
        num = int(input(f'nhap so nguyen thu {i + 1} la : '))
        lisst.append(num)
    return lisst

c = int(input('so luong phan tu la : '))
a = list(map(lambda x: x ** 2, make_list(c)))
print(a)