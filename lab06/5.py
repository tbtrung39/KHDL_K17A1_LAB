a =[]
so_tu_cho= 12345 

for _ in range(1000):
    seed = (1103515245 * so_tu_cho + 12345) % 2**31
    b= (seed // 65536) % 32768
    b = 1 + (b % 99999)
    a.append(b)

print(a)