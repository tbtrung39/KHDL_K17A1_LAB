#7
# viet chuong trinh sinh ra 2 tap hop a va b
a=set(input("moi nhap tap hop a:"))
b=set(input("moi nhap tap hop b:"))
# liet ke cac phan tu chung
phan_tu_chung=a.intersection(b)
#in ra man hinh
print("cac phan tu chung cua a va b la:",phan_tu_chung)