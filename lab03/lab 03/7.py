#Viết chương trình tính tổng nghịch đảo của n số nguyên đầu tiên.
n=int(input("moi nhap so nguyen n:"))
for i in range(1,n+1):
    total=0
    total+=1/i
print("tong cac so nghich dao cua n so nguyen la:",total)