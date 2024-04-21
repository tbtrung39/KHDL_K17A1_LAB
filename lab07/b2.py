Numbers = []
A= set()
while True:
    x= int(input("nhap vao cac so nguyen: "))
    hoi = input("nhap 1 de tiep tuc, 0 de ngung nhap")
    x= int(x)
    Numbers.append(x)
    A.add(x)
    if hoi == "0":
        break
print("danh sach numbers la: ",Numbers)
print("tap hop A la: ",A)