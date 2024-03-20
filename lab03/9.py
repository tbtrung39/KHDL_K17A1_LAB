#Viết chương trình nhập n là số nguyên dương. Nếu n<=0 thì dừng chương trình. Sau đó tính các tổng bt sau
n=int(input("moi nhap so nguyen duong n:"))
if n<0:
    print("ket thuc phuong trinh")
# trinh tong cac bieu thuc s4,s5,s6
else:
    # tinh tong s4
    s4=0
    for i in range(1,n+1):
        s4+=i**2
    print("phuong trinh cua s4 la:",s4)
    # tinh tong s5
    s5=0
    for i in range(1,2*n+2,2):
        s5+=(i)**3
    print("phuong trinh cua s5 la:",s5)
    # tinh tong cua s6
    s6=0
    for i in range(2,2*n+1,2):
        s6+=(i)**4
    print("phuong trinh cua s6 la:",s6)
    # xuat ra man hinh
    print("tong cua s4 la:",s4)
    print("tong cua s5 la:",s5)
    print("tong cua s6 la:",s6)