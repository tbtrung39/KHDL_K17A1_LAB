import random
so_ngau_nhien = [x for x in range(201) if x % 5 == 0 and x % 7 == 0]
so_chia_het = random.choice(so_ngau_nhien)
print("Số ngẫu nhiên chia hết cho cả 5 và 7 từ 0 đến 200 là:", so_chia_het)
