n=int(input("Nhập số nguyên dương n: "))
print ("Dạng phân tích thừa số nguyên tố của",n,"la:")
thua_so_nguyen_to=[]
i=2
while n>1:
    if n % i == 0:
        thua_so_nguyen_to.append(i)
        n//=i
    else:
        i += 1
for thua_so in thua_so_nguyen_to:
    print(thua_so, end="*")