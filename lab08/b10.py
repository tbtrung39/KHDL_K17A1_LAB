n = int(input("Nhập số n: "))
uoc_so = []
for i in range(1, n+1):
    if n % i == 0:
        uoc_so.append(i)
print(uoc_so)