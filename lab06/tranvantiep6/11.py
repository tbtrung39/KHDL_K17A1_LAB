import random 

n = int(input("Nhap mot so nguyen : "))
A = [random.randint(1, n) for _ in range(1,n + 1)]
# danh sach B chua cac phan tu chia het cho 3 nhưng khong chia het cho 5 
B = [i for i in A if i % 3 == 0 and i %  5 == 1]
print(B)
# danh sach C voi cac phan tu la binh phuong cua A : 
C = [j*2 for j in A]
print(C)
# danh sach D gom cac phan tu lay ngau nhien tu danh sach A ma chia het cho 3  :
list_random = random.sample(A, n)
D = [a for a in list_random if a % 3 == 0 ]
print(D)
