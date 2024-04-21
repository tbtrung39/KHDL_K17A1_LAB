phan_tu=set()
while True:
    n= input("nhap phan tu (nhan ESC de thoat): ")
    if n == "ESC":
        break
    phan_tu.add(n)
phan_tu_moi = phan_tu.copy()
for i in phan_tu_moi:
    if i.isdigit():
        phan_tu.remove(i)
print(phan_tu)