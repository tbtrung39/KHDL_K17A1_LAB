#Viết chương trình tính tổng nghịch đảo của n số nguyên đầu tiên.
n=int(input("moi nhap so nguyen duong n:"))
total=0
for i in range(1,n+1):
    total+=1/i
print("tong nghich dao cua n so nguyen dau tien la :",total)