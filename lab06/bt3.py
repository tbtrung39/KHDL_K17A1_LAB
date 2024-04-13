danh_sach = []
while True:
    phan_tu = int(input("Nhập phần tử (nhập 0 để kết thúc): "))
    if phan_tu == 0:
        break
    danh_sach.append(phan_tu)
print(danh_sach)
danh_sach_moi = sorted(danh_sach,reverse=True)
print("Danh sách sau khi chuyển các phần tử dương lên đầu: ",danh_sach_moi)
m = int(input("Nhập số m: "))
danh_sach.insert(0,m)
danh_sach.append(m)
danh_sach.insert(5,m)
print("Danh sách sau khi chèn m: ",danh_sach)