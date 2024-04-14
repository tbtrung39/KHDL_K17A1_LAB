import random
tong = 0
a = []
while True:
    i = random.randint(0,100000)
    tong += i
    a.append(i)
    if len(a) >= 1000:
        break
print("Danh sach 1000 so ngau nhien la:",a)
print(f"Sap xep theo thu tu tang dan {sorted(a,reverse=True)}")
a.sort()
print(f"Sap xep theo thu tu tang dan {a}")