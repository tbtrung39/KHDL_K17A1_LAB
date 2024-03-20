#1. Viết chương trình nhập n là số nguyên dương. Nếu n<=0 thì yêu cầu nhập lại....
n=int(input("moi nhap so nguyen duong n:"))
s4=0
s5=0
s6=0
while n>0:
    for i in range(1,n+1):
        s4+=i**2
    if i%2!=0:
        s5+=i**3
    if i%2==0:
        s6+=i**4
        break
print("tong cua s4 la :",s4)
print("tong cua s5 la :",s5)
print("tong cua s6 la :",s6)

    