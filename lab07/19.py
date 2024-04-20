tu_dien=dict()
while True:
    print("Chương trình thêm thông tin nhân viên")
    ma_nv=input("Nhập mã nhân viên:")
    ten_nv=input("Nhập họ tên nhân viên:")
    nam_sinh=int(input("Nhập năm sinh:"))
    luong=float(input("Nhập lương nhân viên:"))
    hoi=input("có tiếp tục nhập thông tin không:(Y/N)")
    tu_dien.update({ma_nv:[ten_nv,f"năm sinh:{nam_sinh},luong]})
    if hoi=="N":
       break
print(tu_dien)
x=input("Nhập mã sinh viên cần tìm:")
print(tu_dien[x])
y=input("Nhập mã nhân viên muốn tăng lương:")
tu_dien[y][2]+=100000
print(tu_dien[y])    
z=input("Nhập mã nhân viên muốn xóa:")
tu_dien[z]=tu_dien[z].clear()
print(tu_dien)