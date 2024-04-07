chuoi_a= input("Nhap chuoi ki tu:")

chuoi_b=""
for i in chuoi_a:
    if i.isdigit():
        chuoi_b += i

print("Chuoi sau khi loc so la: ",chuoi_b)

n=int(chuoi_b)

tong=0
for i in range(1,n):
    if n % i == 0:
        tong += i
if tong == n:
    print(n,"la so hoan hao")
else:
    print(n,"la so khong hoan hao")