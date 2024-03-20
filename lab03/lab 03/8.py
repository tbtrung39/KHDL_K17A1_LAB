
#Viết chương trình nhập n là số nguyên dương. Nếu n<=0 dừng chương trình. Sau đó tính các tổng sau:
n=int(input("moi nhap so nguyen n:"))
if n<=0:
    print("ket thuc chuong trinh")
else:
    #tinh tong s1
    s1=sum(range(1,n+1))
    #tinh tong s2
    s2=sum(range(1,2*n+2,2))
    #tinh tong s3
    s3=sum(range(1,2*n+1,2))
    print("tong cua s1 la:",s1)
    print("tong cua s2 la:",s2)
    print("tong cua s3 la:",s3)