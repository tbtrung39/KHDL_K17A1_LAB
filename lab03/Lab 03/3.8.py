'''
Viết chương trình nhập n là số nguyên dương. 
Nếu n<=0 dừng chương trình.
Sau đó tính các tổng sau:
a) S1 = 1 + 2 + 3 + … + n
b) S2 = 1 + 3 + 5 + … + (2n+1)
c) S3 = 2 + 4 + 6 + … + 2n
'''
n = int(input("nhập số a:"))
sum = 0
for i in range(1,n+1):
    sum += i
print(sum)
# b
n = int(input("nhập số a:"))
sum = 0
for i in range(1,2*n+1):
    sum += i
print(sum)
# c
n = int(input("nhập số a:"))
sum = 0
for i in range(1,2*n):
    sum += i
print(sum)