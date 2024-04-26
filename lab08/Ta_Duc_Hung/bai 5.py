def ucln(x,y):
    while y!= 0:
        x,y = x , x % y
        return x
    
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
uoc_chung = ucln(x,y)
print(uoc_chung)