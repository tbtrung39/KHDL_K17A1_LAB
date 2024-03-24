'''
Viết chương trình nhập vào một số nguyên dương rồi xuất ra dạng phân tích thừa số nguyên tố của số đó.
'''
n= int(input("Nhap so nguyen duong n: "))
print("Dang phan tich thua so nguyen to cua",n,"la:")
thua_so_nguyen_to = []
i=2
while n>1:
    if n % i == 0:
        thua_so_nguyen_to.append(i)
        n//=i
    else:
        i += 1
for thua_so in thua_so_nguyen_to:
    print(thua_so,end="")