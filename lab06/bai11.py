import random
n = int(input("số lượng số có trong danh sách: "))
list = []
for i in range(n):
    pt = int(input(f"nhập vào phần tử thứ {i+1}: "))
    list.append(pt)
#ý thứ 1
B = [j for j in list if j % 3 == 0 and j % 5 != 0]
print(f"danh sách các số chia hết cho 3 nhưng không chia hết cho 5 là {B}")
#ý thứ 2
newlist = []
for num in list:
    nums = num**2
    newlist.append(nums)
C = [x for x in newlist if x >= 0 ]
print(f"danh sách các số bình phương của list a là {C}")
#ý thứ 3
while True:
    d = random.choice(list)
    D = [d for d in list if d % 3 == 0]
    break
print(f"danh sách số ngẫu nhiên chia hết cho 3 lấy từ list gốc là {D}")