n = int(input("Nhập năm cần kiểm tra: "))
m = int(input("Nhập số tháng: "))
if (n % 400 == 0) or ((n % 4 == 0) and (n % 100 != 0)):
      print("Năm", n, "là năm nhuận")
else:
      print("Năm", n, "không phải là năm nhuận")

if m ==4 or m==6 or m==9 or m ==11:
        print("Số ngày tối đa của tháng", m,"năm",n, "là: 30 ngày ")
elif m == 2:
    if (n % 400 == 0) or ((n % 4 == 0) and (n % 100 != 0)) :
            print("Số ngày tối đa của tháng 2 năm",n,"là: 29")
    else:
            print("Số ngày tối đa của tháng 2 năm",n,"là: 28")
else: 
        print("Số ngày tối đa của tháng ", m, "năm", n, "là: 31 ngày")
      
        