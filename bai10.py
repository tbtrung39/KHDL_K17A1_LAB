import random 
num = [x for x in range(201) if x % 5 ==0 and x % 7 == 0]
snn = random.choice(num)
print("số ngẫu nhiên chia hết 5 vs 7 : ", snn)