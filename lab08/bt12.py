def luong_nhan_vien():
    n = input("Nhập vào tên nhân viên: ")
    qq = input("Nhập vào quê quán của nhân viên: ")
    tn = int(input("Nhập vào thâm niên của nhân viên tính theo năm: "))
    luong = 6000000 * tn * (5/100)
    return n,qq,tn,luong
x = int(input("Nhập vào số lượng nhân viên cần nhập thông tin: "))
list = []
for i in range(x):
    list.append(luong_nhan_vien())
print(f"Danh sách thông tin cơ bản của {x} nhân viên nhập từ bàn phím lần lượt từ tên,quê quán, thâm niêm và lương {list}")