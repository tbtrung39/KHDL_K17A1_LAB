# Nhập vào số thứ trong tuần
so_thu = int(input("Nhập vào số thứ trong tuần (từ 1 đến 7): "))

# Kiểm tra số thứ và in ra tên của ngày tương ứng
if so_thu == 1:
    print("Sunday")
elif so_thu == 2:
    print("Monday")
elif so_thu == 3:
    print("Tuesday")
elif so_thu == 4:
    print("Wednesday")
elif so_thu == 5:
    print("Thursday")
elif so_thu == 6:
    print("Friday")
elif so_thu == 7:
    print("Saturday")
else:
    print("Số bạn nhập không hợp lệ. Vui lòng nhập lại từ 1 đến 7.")