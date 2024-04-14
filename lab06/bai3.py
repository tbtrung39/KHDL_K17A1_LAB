#câu 3
danh_sach = []
while True:
    nhap_vao = int(input("Nhập các giá trị: "))
    danh_sach.append(nhap_vao)
    if nhap_vao == 0:
        break
print("Danh sách ban đầu:", danh_sach)
danh_sach_moi = []
for i in danh_sach:
    if i > 0:
        danh_sach_moi.append(i)
for i in danh_sach_moi:
    danh_sach.remove(i)
danh_sach = danh_sach_moi + danh_sach
print("Danh sách sau khi đưa các phần tử dương lên đầu:", danh_sach)
m = int(input("nhập số m:"))
danh_sach.insert(0, m)
danh_sach.insert(5,m)
danh_sach.append(m)
print("Danh sách sau khi chèn số m vào đầu,vị trí thứ 5 và cuối:", danh_sach)















































