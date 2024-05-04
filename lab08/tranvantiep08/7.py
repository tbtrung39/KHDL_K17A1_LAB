def find_value(a, b, c) : 
    value_max = max(a, b, c)
    value_min = min(a, b, c)
    return value_max, value_min

c = int(input('nhap so dau : '))
d = int(input('nhap so thu hai : '))
e = int(input('nhap so thu ba : '))
print(f'gia tri (max, min) cua ba so la : ', find_value(c, d, e))
        