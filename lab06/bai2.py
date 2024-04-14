#2
danhsach=[]
n=int(input("nhập n: "))
for i in range(n):
    a=int(input(f" nhập giá trị thứ {i+1} : "))
    danhsach.append(a)
print("danh sách : ", danhsach)
danhsachmoi=sorted(danhsach,reverse=True)
so_lon_t2=danhsachmoi[1]
vitri=danhsach.index(so_lon_t2)
print("số lớn t2" , so_lon_t2)
print("vị trí ", vitri)
danhsachlientiep = 0  
danhsachhientai = 0  
for num in danhsach:
        if num > 0:
            danhsachhientai += 1
            danhsachlientiep = max(danhsachlientiep, danhsachhientai)
        else:
            danhsachhientai = 0
print("Số lượng số dương liên tiếp nhiều nhất trong danh sách là:", danhsachlientiep)
soluonglientiepmax = 0  # Số lượng số dương liên tiếp có tổng lớn nhất
current_count = 0       # Số lượng số dương liên tiếp hiện tại
tonglientiepmax = 0     # Tổng của số dương liên tiếp có tổng lớn nhất
tonglientiephientai = 0 # Tổng của số dương liên tiếp hiện tại

for num in danhsach:
    if num > 0:
        danhsachhientai += 1
        tonglientiephientai += num
        if tonglientiephientai > tonglientiepmax:
            tonglientiepmax = tonglientiephientai
            soluonglientiepmax =danhsachhientai
    else:
        danhsachhientai = 0
        tonglientiephientai = 0
print("Số lượng số dương liên tiếp có tổng lớn nhất trong danh sách là:", soluonglientiepmax)