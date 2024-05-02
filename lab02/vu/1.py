a = int(input("Nhập tháng từ (1-12) là:"))
if a == 1 or a == 3 or a == 7 or a == 5 or a == 8 or a == 10 or a == 12:
    print("Tháng",a,"có 31 ngày")
if a == 4 or a == 6 or a == 9 or a == 11:
    print("Tháng",a,"có 30 ngày")
if a == 2:
    print("Tháng",a,"có 28 hoặc 29 ngày")