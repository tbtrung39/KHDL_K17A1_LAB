#10
import random
chon = [x for x in range(201) if x % 5 == 0 and x % 7 == 0]
random_number = random.choice(chon)
print("Số ngẫu nhiên chia hết cho cả 5 và 7 từ 0 đến 200 là:", random_number)