ttnv = {}
n = int(input("nhập vào số lượng nhân viên: "))
#A & B
for i in range(n):
    mnv = int(input(f"nhập vào mã nhân viên gồm 4 ký tự thứ {i + 1}: "))
    mnv = str(mnv)
    while len(mnv) != 4:
        print("mã nhân viên phải gồm 4 ký tự")
        mnv = int(input(f"nhập lại mã nhân viên gồm 4 ký tự thứ {i + 1}: "))
        mnv = str(mnv)
    name = str(input(f"nhập vào tên nhân viên thứ {i + 1}: "))
    date = int(input(f"nhập vào năm sinh của nhân viên thứ {i + 1}: "))
    salary = int(input(f"nhập vào lương của nhân viên thứ {i + 1}: "))
    ttnv[mnv] = {"name": name, "date_of_birth": date, "salary": salary} 
# C
x = input("mã nhân viên cần tìm: ")
if x in ttnv:
    nv = ttnv[x]
    print("Thông tin nhân viên:")
    print(f"Mã nhân viên: {x}")
    print(f"Tên nhân viên: {nv['name']}")
    print(f"Năm sinh: {nv['date_of_birth']}")
    print(f"Lương: { nv['salary']}")
else:
    print("không tồn tại nhân viên này")
# D
y = input("nhân viên được tăng lương: ")
if y in ttnv:
    ttnv[y]["salary"] += 1000000
    print(f"Lương mới của {y} là: {ttnv[y]['salary']}")
    print(f"Thông tin sau khi thay đổi là {ttnv}")
else:
    print("không tồn tại nhân viên này")
# E
z = int(input("nhập vào mã nhân viên cần xóa; "))
if z in ttnv:
    ttnv.pop(z)
    print(f"nhân viên {z} đã bị sa thải danh sách mới {ttnv}")
else:
    print("không tồn tại nhân viên này")