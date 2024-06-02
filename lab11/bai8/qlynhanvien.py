import csv
soluong = int(input("nhap so nhan vien can them thong tin: "))
count = 0
danh_sach = []
while count <soluong:
    lst  = []
    name = input("nhap ten: ")
    he_so_luong = int(input("nhap he so luong: "))
    luong = he_so_luong *1490000
    chuc_vu = input("nhap chuc vu 'TP,PP,NV': ")
    if chuc_vu == "TP":
        thuc_linh = luong + 1000000
    elif chuc_vu == "PP":
        thuc_linh = luong +700000
    elif chuc_vu == "NV":
        thuc_linh == luong + 300000
    else:
        print("nhap sai chuc vu")
        break
    lst.append(name)
    lst.append(he_so_luong)
    lst.append(luong)
    lst.append(chuc_vu)
    lst.append(thuc_linh)
    danh_sach.append(lst)
    count +=1
print(danh_sach)
with open(file =r"bai8\libs\ds_nhanvien.csv", mode= "w") as f:
    write = csv.writer(f)
    sort = sorted(danh_sach,key= lambda x: x[4],reverse=True)
    for i in sort:
        write.writerow(i)