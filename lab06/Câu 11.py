'''
Viết chương trình tạo một danh sách A có n phần tử là số nguyên được nhập từ bàn phím. 
Sử dụng List Comprehension thực hiện các yêu cầu sau:
a. Tạo ra một danh sách B chứa các phần tử chia hết cho 3 nhưng không chia hết cho 5 từ danh sách ban đầu.
 In kết quả ra màn hình.
b. Tạo một danh sách C với các phần tử là bình phương của danh sách A.
c. Tạo ra danh sách D gồm các phần tử lấy ngẫu nhiên từ danh sách A mà chia hết cho 3.
'''
import random

n = int(input("Nhập số lượng phần tử của danh sách A: "))
A = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]

#a. Tạo danh sách B chứa các phần tử chia hết cho 3 nhưng không chia hết cho 5 từ danh sách ban đầu
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("Danh sách B:", B)

#b. Tạo danh sách C với các phần tử là bình phương của danh sách A
C = [x ** 2 for x in A]
print("Danh sách C:", C)

#c. Tạo danh sách D gồm các phần tử lấy ngẫu nhiên từ danh sách A mà chia hết cho 3
D = random.sample([x for x in A if x % 3 == 0], k=min(3, len(A)))
print("Danh sách D:", D)

