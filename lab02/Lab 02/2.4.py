'''
Nhập vào 1 số nguyên, yêu cầu xuất ra chữ số hàng trăm của số đó, nếu không có thì xuất ra 0.
'''
number = int(input("Nhập vào một số nguyên: "))

# Tính chữ số hàng trăm
chu_so_hang_tram = (number // 100) % 10

# Kiểm tra nếu có chữ số hàng trăm
if chu_so_hang_tram != 0:
    print("Chữ số hàng trăm của số", number, "là:", chu_so_hang_tram)
else:
    print("Số", number, "không có chữ số hàng trăm.")