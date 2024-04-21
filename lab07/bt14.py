tu_dien = {}

# Tạo từ điển
for i in range(1, 101):
    chuoi_nhi_phan = bin(i)[2:]  # Chuyển số i sang chuỗi nhị phân, bỏ qua '0b' ở đầu
    tu_dien[i] = chuoi_nhi_phan

# In ra từ điển
print("Từ điển số nhị phân:")
for key, value in tu_dien.items():
    print(key, ":", value)
