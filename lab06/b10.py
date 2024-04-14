import random

so_ngau_nhien = random.choice([x for x in range(201) if x % 5 == 0 and x % 7 == 0])

print("Số ngẫu nhiên chia hết cho cả 5 và 7 từ 0 đến 200 là:", so_ngau_nhien)