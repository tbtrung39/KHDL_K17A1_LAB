dict = {}
for i in range(1,101):
    so = ""
    num = i
    while num > 0:
        so = str(num % 2) + so
        num //= 2
    dict[i] = so
for tu_dien,nhi_phan in dict.items():
    print(tu_dien,f"{nhi_phan}")