#Viết chương trình tính tổng bậc 3 của n số nguyên đầu tiên. In kết quả ra màn hình.
n=int(input("moi nhap so nguyen n:"))
total=0
for i in range(1,n+1):
    total+=i**3
print("tong bac 3 cua n so nguyen dau tien la:",total)