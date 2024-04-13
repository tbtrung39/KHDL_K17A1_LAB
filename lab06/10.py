import random
num= [x for x in range(201) if x % 5 ==0 and x % 7 == 0]
ran_num = random.choice(num)
print("số ngẫu nhiên chia hết cho 5 va 7 : ",ran_num)