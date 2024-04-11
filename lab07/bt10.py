# Nhập hai số m và n từ người dùng
m = int(input("Nhập số m: "))
n = int(input("Nhập số n: "))

# Chuyển m và n thành chuỗi để dễ xử lý
m_str = str(m)
n_str = str(n)

# Khởi tạo một set để lưu trữ các chữ số chung
common_digits = set()

# Duyệt qua từng chữ số trong m
for digit in m_str:
    # Nếu chữ số đó cũng xuất hiện trong n và chưa được thêm vào set common_digits
    if digit in n_str and digit not in common_digits:
        # Thêm chữ số đó vào set
        common_digits.add(digit)

# Duyệt qua từng chữ số trong n
for digit in n_str:
    # Nếu chữ số đó cũng xuất hiện trong m và chưa được thêm vào set common_digits
    if digit in m_str and digit not in common_digits:
        # Thêm chữ số đó vào set
        common_digits.add(digit)

# Tính tổng các chữ số chung
sum_common = sum(int(digit) for digit in common_digits)

# In ra tổng các chữ số chung
print("Tổng các chữ số chung của m và n là:", sum_common)
