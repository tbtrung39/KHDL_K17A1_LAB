import random

# Sử dụng list comprehension để tạo ra một list chứa các số chia hết cho cả 5 và 7 từ 0 đến 200
numbers_divisible_by_5_and_7 = [num for num in range(201) if num % 5 == 0 and num % 7 == 0]

# Nếu list không rỗng, chọn một số ngẫu nhiên từ list và in ra
if numbers_divisible_by_5_and_7:
    random_number = random.choice(numbers_divisible_by_5_and_7)
    print("Số ngẫu nhiên chia hết cho cả 5 và 7 từ 0 đến 200 là:", random_number)
else:
    print("Không có số nào chia hết cho cả 5 và 7 từ 0 đến 200.")