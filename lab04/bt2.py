n = int(input("Nhập số lượng phần tử của dãy:  "))
i = 1 #biến sử dụng để đếm số vòng lặp
tong_a = 0
tong_b = 0
tong_c = 0
ktr_dau= 1 #biến kiểm tra dấu vì sau mỗi lần lặp thay đổi từ -1 sang 1 và ngược lại

while i <= n: #nếu số vòng lặp vượt quá số phần tử thì vòng lặp sẽ dừng lại
    tong_a += ktr_dau * (1/i)
    ktr_dau *= -1
    i += 1
print(f"tổng của dãy a bằng {tong_a}")
while i <= n:
    tong_b += 1/(i*(i+1))
    i += 1
print(f"tổng của dãy b  bằng {tong_b}")
while i <= n:
    tong_c += 1/(i**0.5)
    i += 1
print(f"tổng của dãy b  bằng {tong_c}")
