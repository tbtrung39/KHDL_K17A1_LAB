#câu 4
danh_sach = []
nhap_vao_k = int(input("Nhập vào số k: "))

# Nhập các phần tử cho danh sách
while True:
    nhap_vao = int(input("Nhập các giá trị (nhập 0 để kết thúc): "))
    if nhap_vao == 0:
        break
    danh_sach.append(nhap_vao)

print("Danh sách ban đầu:", danh_sach)

# Thêm [1, 2, 3] vào đầu, cuối và vị trí thứ 5
danh_sach.insert(0,[1,2,3])
danh_sach.insert(5,[1,2,3])
danh_sach.append([1,2,3])
print(f"Danh sách sau khi chèn vào vị trí đầu tiên, thứ 5 và cuối cùng là: {danh_sach}")
# Xóa tất cả các lần xuất hiện của số k
danh_sach = [x for x in danh_sach if x != nhap_vao_k]
print(f"Danh sách sau khi loại bỏ {nhap_vao_k}: {danh_sach}")
#sắp xếp theo thứ tự tăng dần
danh_sach.sort()
print(danh_sach)
#sắp xếp theo thứ tự giảm dần
danh_sach.reverse()
print(danh_sach)