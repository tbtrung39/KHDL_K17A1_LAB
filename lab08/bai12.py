def nv():
    n = input("nhập vào tên nhân viên : ")
    qq = input("nhập vào quê quán của nhân viên: ")
    tn = int(input(f"nhập vào thâm niên của nhân viên tính theo năm: "))
    luong = 6000000 * tn * (5/100)
    return n,qq,tn,luong
x = int(input("nhập vào số lượng nhân viên cần nhập thông tin: "))
lst = []
for i in range(x):
    lst.append(nv())
print(f"Danh sách thông tin cơ bản của {x} nhân viên nhập từ bàn phím lần lượt từ tên,quê quán, thâm niêm và lương {lst}")