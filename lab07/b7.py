A= set()
B= set()
while True:
    n=input("nhap phan tu A: ")
    m=input("nhap phan tu B: ")
    A.add(n)
    B.add(m)
    hoi=input("nhap 1 de tiep tuc, nhap 0 de dung nhap: ")
    if hoi == "0":
        break

phan_tu_chung = A & B
print("phan tu chung cua A va B la: ",phan_tu_chung)
