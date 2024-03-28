def demuoc(a):
    tong=0
    for i in range(1,a):
        if a%i==0:
            tong+=i
    return tong
n = int(input("Nhập vào n:"))
for i in range(1,n):
    if demuoc(i)==i:
        print(f"{i} là số hoàn hảo")