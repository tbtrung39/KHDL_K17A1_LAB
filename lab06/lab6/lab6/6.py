import random

list = []
for i in range(1000):
    ran = random.randint(1,9999)
    list.append(ran)
print("Danh sách sd sorted:",sorted(list))

for i in range(len(list)):
    for j in range(len(list)-1):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] =  list[j + 1],  list[j]

print("Danh sách không sử dụng sorted: ", sorted(list))