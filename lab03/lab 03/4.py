#Viết chương trình in ra tất cả các số nguyên tố bé hơn hoặc bằng n.
n=int(input("moi nhap so nguyen n:"))
print("cac so nguyen to nho hon hay bang n la:")
for num in range(1,n+1):
    j=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            j=False
            break
        if j:
            print(num,end="")