import random
a = [i for i in range(0,201) if i % 5 == 0 and i % 7 == 0]
print(a)
b = random.choice(a)
print(f"số ngẫu nhiên chia hết cho cả 5 và 7 là {b}")