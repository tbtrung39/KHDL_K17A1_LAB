import random
numbers = [num for num in range(0,201) if num %5 ==0 and num%7 ==0]
random_number = random.choices(numbers)
print(random_number)