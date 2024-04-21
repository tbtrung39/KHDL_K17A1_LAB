A= set()
while True:
    x= int(input("nhap vao cac so nguyen: "))
    hoi = input("nhap 1 de tiep tuc, 0 de ngung nhap")
    A.add(x)
    if hoi == "0":
        break
print("phan tu lon nhat cua A la:",max(A))
print("phan tu nho nhat cua A la:",min(A))
print("tong cac phan tu cua A la:",sum(A))