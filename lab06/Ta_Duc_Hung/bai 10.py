# bài 10 
import random
random_numbers=[num for num in range(201) if num % 5 ==0 and num % 7 == 0 ]
random_number=random.choice(random_numbers)
print("danh sách số ngẫu nhiên chia hết cho 5 và 7 là :",random_numbers)
print("số ngẫu nhiên được chọn là :",random_number)

