# Nhập vào số tháng trong năm
so_thang = int(input("Nhập vào số tháng trong năm (từ 1 đến 12): "))

# Kiểm tra số tháng và in ra tên của tháng tương ứng
if so_thang == 1:
    print("January")
elif so_thang == 2:
    print("February")
elif so_thang == 3:
    print("March")
elif so_thang == 4:
    print("April")
elif so_thang == 5:
    print("May")
elif so_thang == 6:
    print("June")
elif so_thang == 7:
    print("July")
elif so_thang == 8:
    print("August")
elif so_thang == 9:
    print("September")
elif so_thang == 10:
    print("October")
elif so_thang == 11:
    print("November")
elif so_thang == 12:
    print("December")
else:
    print("Số bạn nhập không hợp lệ. Vui lòng nhập lại từ 1 đến 12.")