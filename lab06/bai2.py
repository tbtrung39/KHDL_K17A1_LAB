danh_sach = []
while True:
    nhap_vao = int(input("nhập các giá trị:"))
    danh_sach.append(nhap_vao)
    nhap_tiep = input("bạn có muốn nhập tiếp không?(y/n):")
    if nhap_tiep == "n":
        break
print(danh_sach)
danh_sach.sort()
print(f"phần tử lớn thứ hai trong danh sách là:{danh_sach[int(len(danh_sach)-2)]}")
print(f"vị trí của phần tử lớn thứ 2 là:{int(len(danh_sach)-2)}")
# Tính số lượng các số nguyên dương liên tiếp nhiều nhất
max_lien_tiep = 0
hien_tai_lien_tiep = 0
for so in danh_sach:
    if so > 0:
        hien_tai_lien_tiep += 1
    else:
        max_lien_tiep = max(max_lien_tiep, hien_tai_lien_tiep)
        hien_tai_lien_tiep = 0

max_lien_tiep = max(max_lien_tiep, hien_tai_lien_tiep)

print(f"Số lượng các số nguyên dương liên tiếp nhiều nhất trong danh sách là: {max_lien_tiep}")