n = int(input("Nhập vào n:"))
tong=0
s=str(n)
l=len(s)
for i in range(1,l+1):
    tong+=int(s[i-1])
print(tong)