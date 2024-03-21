# Nhập số nguyên dương từ người dùng
number = int(input("Nhập một số nguyên dương: "))

# Khởi tạo danh sách để lưu các thừa số nguyên tố
prime_factors = []

# Phân tích số thành các thừa số nguyên tố
factor = 2
while number > 1:
    if number % factor == 0:
        prime_factors.append(factor)
        number //= factor
    else:
        factor += 1

# In ra dạng phân tích thừa số nguyên tố
if len(prime_factors) == 0:
    print("Số này không có thừa số nguyên tố.")
else:
    print("Dạng phân tích thừa số nguyên tố của số đó là:", end=" ")
    for i in range(len(prime_factors)):
        if i == len(prime_factors) - 1:
            print(prime_factors[i])
        else:
            print(prime_factors[i], "*", end=" ")