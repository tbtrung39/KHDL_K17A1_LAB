def luong(a,b,c):
    luong_thang=a/b*c
    return luong_thang
a=float(input("Lương thỏa thuận: "))
b=float(input("số ngày làm việc trong tháng: "))
c=float(input("số ngày đi làm thực tế: "))
ho_ten_nv=input("Nhập họ tên: ")
luong_thang=luong(a,b,c)
print("Họ và tên nhân viên: ",ho_ten_nv)
print("Lương của nhân viên là: ",luong_thang)