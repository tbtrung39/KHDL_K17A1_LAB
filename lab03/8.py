a = int(input("Nhập giá trị a là: "))
s1 = 0
s2 = 0
s3 = 0
for i in range(1,a+1):
    s1 += i
    if a <= 0:
        break

for j in range(1, a+1, 2):
    s2 += j
    if a <= 0:
        break

for k in range(0, a+1 ,2):
    s3 += k
    if a <= 0:
        break

print("s1= ", s1)
print("s2= ", s2)
print("s3= ", s3)