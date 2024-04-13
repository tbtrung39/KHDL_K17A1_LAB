import random

numbers = [num for num in range(0,201)if num % 5 == 0 and num % 7 == 0]
random_number = random.choice(numbers)
print(f"So ngau nhien chia het cho 5 va 7 tu 0 den 200 la:{random_number}")