str = input("Nhập chuỗi kí tự: ")
number_str = '' #biến number này để lưu chuỗi số
#lọc ký tự là số từ chuỗi nhập vào
for char in str:
    if char.isdigit():
        number_str += char
#in ra chuỗi số đã lọc
print(f"chuỗi số sau khi xoá ký tự không phải là số là {number_str}")

#kiểm tra số hoàn hảo
if number_str.isdigit():
    number = int(number_str)
    tong_uoc = 0 #số hoàn hảo là số chia hết cho tổng các ước của nó ví vụ 6 % 1 , 2 ,3
    for i in range(1, number):
        if number % i ==0:
            tong_uoc += 1
    if tong_uoc ==number:
        print(f"{number_str} là chuỗi hoàn hảo")
    else:
        print(f"{number_str} không là chuỗi hoàn hảo")
else:
    print(f"{number_str} không là chuỗi số")