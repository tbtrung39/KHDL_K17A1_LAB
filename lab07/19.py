ttnv = {}
n = int(input("Nhap vao so luong nhan vien: "))
for i in range(n):
    mnv = int(input(f"Nhap vao ma nhan vien gom 4 kytu thu {i + 1}: "))
    mnv = str(mnv)
    while len(mnv) !=4:
        print("Ma nhan vien phai gom 4 ky tu")
        mnv = int(input(f"Nhap lai ma nhan vien gom 4 ký tu thu {i + 1}"))
        mnv = str(mnv)
    name = str(input(f"Nhap vao ten nhan vien thu {i + 1}: "))
    date = int(input(f"Nhap vao nam sinh cua nhan vien thu {i + 1}: "))
    salary = int(input(f"Nhap vao luong cua nhan vien thu {i + 1}: "))
    ttnv[mnv] = {"name": name, "date_of_birth": date, "salary": salary}
x = input("Ma nhan vien can tim: ")
if x in ttnv:
    nv = ttnv[x]
    print("Thong tin nhan vien: ")
    print(f"Ma nhan vien: {x}")
    print(f"Ten nhan vien: {nv['name']}")
    print(f"Nam sinh: {nv['date_of_birth']}")
    print(f"Luong: {nv['salary']}")
else:
    print("Khong ton tai nhan vien nay")
y = input("Nhan vien duoc tang luong: ")
if y in ttnv:
    ttnv[y]["salary"] += 1000000
    print(f"Luong moi cua {y} la: {ttnv[y]['salary']}")
    print(f"Thong tin sau khi thay doi la: {ttnv}")
else:
    print("Khong ton tai nhan vien nay")
z = int(input("Nhap vao ma nhan vien can xoa: "))
if z in ttnv:
    ttnv.pop(z)
    print(f"Nhan vien {z} da  bi sa thai danh sach moi {ttnv}")
else:
    print("Khong ton tai nhan vien nay")