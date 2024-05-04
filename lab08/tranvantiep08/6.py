def ucln(a, b):
    for i in range(min(a, b), 1, -1): 
        if a % i == 0 and b % i == 0 : 
            return i
    return 1

c = int(input('nhap so dau : '))
d = int(input('nhap so thu hai : '))
print(f'boi chung nho nhat cua {c} va {d} la : ', (c * d) / ucln(c, d))
