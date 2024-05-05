def dao_nguoc_so(n, reversed_n=0):
    if n == 0:
        return reversed_n
    else:
        last_digit = n % 10  # Lấy chữ số cuối cùng của số n
        new_reversed_n = (reversed_n * 10) + last_digit  # Thêm chữ số cuối cùng vào đầu reversed_n
        remaining_n = n // 10  # Bỏ đi chữ số cuối cùng của số n
        return dao_nguoc_so(remaining_n, new_reversed_n)

# Nhập số từ người dùng
n = int(input("Nhập một số nguyên dương: "))
# Gọi hàm để đảo ngược số và in kết quả
print("Số sau khi đảo ngược là:", dao_nguoc_so(n))