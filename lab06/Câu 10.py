'''
Viết phương trình sử dụng module randor va list comprehension để xuất hiện một số ngẫu nhiên,
chia hết cho 5 và 7, từ 0 đến 200 (gồm cả 0 và 200).
'''
import random

#Tạo danh sách các số chia hết cho cả 5 và 7 từ 0 đến 200 bằng list comprehension
numbers = [x for x in range(201) if x % 5 == 0 and x % 7 == 0]

#Chọn ngẫu nhiên một số từ danh sách đã tạo
random_number = random.choice(numbers)

#In ra màn hình
print("Số ngẫu nhiên chia hết cho cả 5 và 7 từ 0 đến 200 là:", random_number)
