#Viết chương trình nhập vào một số nguyên dương rồi xuất ra dạng phân tích thừa số nguyên tố của số đó.
# Nhập vào số nguyên dương từ người dùng
number = int(input("Nhập vào một số nguyên dương: "))

# In ra dạng phân tích thừa số nguyên tố
print("Phân tích thừa số nguyên tố của", number, "là:")

# Bắt đầu vòng lặp để phân tích thừa số
factor = 2
while factor <= number:
    count = 0
    while number % factor == 0:
        count += 1
        number //= factor
    if count != 0:
        print(factor, "^", count, end=" ")
    factor += 1