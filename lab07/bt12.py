n = int(input("Nhập số nguyên n: "))

# Tạo dictionary
result_dict = {}
for i in range(1, n + 1):
    result_dict[i] = i * i

# In ra dictionary
print("Dictionary:", result_dict)
