import random

random_numbers = [x for x in range(201) if x % 35 == 0]

if random_numbers:

    number = random.choice(random_numbers)

    print("Số ngẫu nhiên chia hết cho cả 5 và 7 là:",number)

else:

    print("Không có số nào chia hết cho cả 5 và 7 trong khoảng từ 0 đến 200.")