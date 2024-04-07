'''Nhập một số tự nhiên n từ bàn phím. Viết chương trình chuyển số n từ hệ cơ số 10 sang 
nhị phân. Kết quả là chuỗi nhị phân'''
n = int(input(" nhap mot so:"))
i = ""
while n>0 :
    so = n%2
    i = str(so) + i
    n //=2
print(i)




'''def decimal_to_binary(decimal_num):
    binary_num = ""
    
    # Chuyển đổi từ thập phân sang nhị phân
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num //= 2
    
    return binary_num

# Nhập số thập phân từ người dùng
decimal_input = int(input("Nhập số thập phân: "))

# Chuyển đổi và in ra kết quả
binary_output = decimal_to_binary(decimal_input)
print("Số nhị phân tương ứng là:", binary_output)
'''