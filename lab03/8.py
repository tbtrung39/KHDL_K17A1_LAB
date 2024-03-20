#Viết chương trình nhập n là số nguyên dương. Nếu n<=0 dừng chương trình. Sau đó tính các tổng sau
n=int(input("moi nhap so nguyen duong n:"))
if n<=0:
    print("ket thuc phuong trinh")
# tinh tong s1,s2,s3
s1=sum(range(1,n+1))
s2=sum(range(1,2*n+2,2))
s3=sum(range(1,2*n+1,2))
# xuat ra man hnh
print("tong cua s1 la:",s1)
print("tong cua s2 la:",s2)
print("tong cua s3 la:",s3)


