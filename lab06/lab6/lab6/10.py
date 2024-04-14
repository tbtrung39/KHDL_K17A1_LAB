import random
random_num = [num for num in range(201) if num % 5 == 0 and num % 7 == 0]
random_number = random.choice(random_num)
print("Danh sách các số ngẫu nhiên chia hết cho 5 vfa 7 từ 0 đến 200.")
print(random_num)
print("Số ngẫu nhiên được chọn:", random_number)