import random
so_ngau_nhien = [x for x in range(201) if x % 35 == 0]
if so_ngau_nhien:
    so = random.choice(so_ngau_nhien)
    print("Số ngẫu nhiên chia hết cho cả 5 và 7 là: ",so)
else:
    print("Không có số nào chia hết cho cả 5 và 7 trong khoảng từ 0 đến 200")