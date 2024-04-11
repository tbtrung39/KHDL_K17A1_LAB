import random
random_numbers = [num for num in range(201) if num % 5 == 0 and num % 7 == 0]
random_selected_number = random.choice(random_numbers)
print("Số ngẫu nhiên chia hết cho cả 5 và 7 từ 0 đến 200 là:", random_selected_number)