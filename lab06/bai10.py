import random
so_ngau_nhien_pham_vi = [i for i in range(0,201) if i % 5 == 0 and i % 7 == 0]
print(f"các số chia hết cho 5 và 7 trong phạm vi 1 đến 200 là:{so_ngau_nhien_pham_vi}")
so_ngau_nhien = random.choice(so_ngau_nhien_pham_vi)
print(f"một số ngẫu nhiên chia hết cho cả 5 và 7 là {so_ngau_nhien}")