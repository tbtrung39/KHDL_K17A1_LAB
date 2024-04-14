lst = []
while True:
    n = int(input("nhap vao ot so tu nhien, 'nhap 0 de duong chuong trinh"))
    if n == 0:
        break
    lst.append(n)

duong = [i for i in lst if i>0]
am = [i for i in lst if i <0]
lst = duong + am
print("list sau khi chuyen cac phhan tu duong len dau la: ",lst)
m =int(input("nhap so nguyen duong de chen`: "))
lst.insert(0,m)
lst.insert(5,m)
lst.append(m)
print(f"danh sach sau khi chen {m} la:",lst)
