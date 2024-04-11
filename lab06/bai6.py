import random
tong = 0
a = []
while True:
    i = random.randint(0,100000)
    tong += i
    a.append(i)
    if len(a) >= 1000:
        break
print(f"danh sách 1000 só ngẫu nhiên là {a}")
print(f"sắp xếp theo thứ tự tăng dần {sorted(a,reverse=True)}")
a.sort()
print(f"sắp xếp theo thứ tự tăng dần {a}")