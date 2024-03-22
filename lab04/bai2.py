import math
tong =0
dau =1
n=2

while True:
    tong+=dau*1/n
    dau *=-1
    n+=1
    if n>1000:
        break
print("S =", tong)

while True:
    tong+=dau*1/n
    n*=(n+1)
    if n>1000:
        break
print("S =", tong)

while True:
    tong+=dau*1/n
    n=math.sqrt(n+1)
    if n>1000:
        break
print("S =", tong)