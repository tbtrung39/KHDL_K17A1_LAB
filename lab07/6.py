n = int(input("Nhap so tu nhien :"))

so_nguyen_to=set()

dem=0
so=2

while dem < n:
    la_so_nguyen_to = True
    for i in range(2, int(so**0.5)+1):
        if so % i ==0:
            la_so_nguyen_to=False
            break
    if la_so_nguyen_to:
        so_nguyen_to.add(so)
        dem+=1
    so +=1

print(f"{n} so nguyen to dau tien la:",so_nguyen_to)
