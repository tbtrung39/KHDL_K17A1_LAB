import random
number=[i for i in range(0,201) if i%5==0 and i%7==0]
random_number=random.choice(number)
print('Số ngẫu nhiêu chia hết cho 5&7:',random_number)