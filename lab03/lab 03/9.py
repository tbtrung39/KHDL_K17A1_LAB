#Viết chương trình nhập n là số nguyên dương. Nếu n<=0 thì dừng chương trình. Sau đó tính các tổng sau bằng vòng lặp for:
n=int(input("moi nhap so nguyen n:"))
if n<=0:
    print("ket thuc chuong trinh")
else:
    #tinh tong s4
    s4=0
    for i in range(1,n+1):
        s4+=i**2
    #tinh tong s5
    s5=0
    for i in range(1,2*n+2,2):
        s5+=i**3
    #tinh tong s6
    s6=0
    for i in range(2,2*n+1,2):
        s6+=i**4
    print("tong cua s4 la:",s4)
    print("tong cua s5 la:",s5)        
    print("tong cua s6 la:",s6)     