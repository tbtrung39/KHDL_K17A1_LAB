import random

list = []
for i in range(1000):
    ran = random.randint(1,9999)
    list.append(ran)
print("Danh sách gồm 1000 số tự nhiên:")
print(list[:10],"....")