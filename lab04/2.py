#2. Tính tổng
n=int(input("moi nhap so nguyen duong n:"))
while n>0:
    s1=0
    for i in range(1,n+1):
        if n%2==0:
            s1+=1/i
        else:
            s1-=1/i
            break
print("tong nghiem cua s1 la:",s1)
# tinh s2
while n>0:
    s2=0
    for i in range(1,n):
        s2+=(1/i*(i+1))
        break
print("phuong trinh cua s2 la:",s2)
#tinh s3
while n>0:
    s3=0
    for i in range(2,n+1):
        s3+=1/i**0.5
        break
print("phuong trinh cua s3 la:",s3)

