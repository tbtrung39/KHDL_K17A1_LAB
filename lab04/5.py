#5. Viết chương trình nhập vào số bất kỳ đến khi nhập số âm thì dừng lại.
while True:
    n=int(input("moi nhap so nguyen duong n:"))
    if n<0:
        print("ket thuc chuong trinh:")
        break
    else:
        print("so nguyen duong nhap duoc la:",n)