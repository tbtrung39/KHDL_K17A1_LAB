n = int(input("nhập số nguyên dương n = "))
day_so_nguyen_to = []
for i in range(0,n+1):
    if i < 2:
        continue
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        day_so_nguyen_to.append(i)
print("dãy n số nguyên tố dầu tiên là :", day_so_nguyen_to)

def ktra_ngto(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        return True
if ktra_ngto(n):
    print("là số nguyên tố")
else:
    print("không là số nguyên tố")