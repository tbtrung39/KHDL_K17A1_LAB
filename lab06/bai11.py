import random
n = int(input("số lượng số trong danh sách: "))
ds = []
for i in range(n):
    pt = int(input(f"nhập vào phần tử thứ {i+1}: "))
    ds.append(pt)
#a
B = [j for j in ds if j % 3 == 0 and j % 5 != 0]
print(f"danh sách các số chia hết cho 3 nhưng không chia hết cho 5 là {B}")
#b
dsms = []
for num in ds:
    nums = num**2
    dsms.append(nums)
C = [x for x in dsms if x >= 0 ]
print(f"danh sách các số bình phương của list a là {C}")
#c
while True:
    d = random.choice(ds)
    D = [d for d in ds if d % 3 == 0]
    break
print(f"danh sách số ngẫu nhiên chia hết cho 3 lấy từ ds gốc là {D}")