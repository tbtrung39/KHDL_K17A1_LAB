print("Bài 4: Giải phương trình")
print("1. Giải phương trình bậc nhất một ẩn")
print("2. Giải phương trình bậc hai")

from package import giaipt

chon = int(input("Nhập chức năng: "))

if chon == 1:
    m = int(input("Nhập hệ số thứ nhất: "))
    n = int(input("Nhập hệ số thứ hai: "))
    giaipt.pt_bac_nhat(m, n)
elif chon == 2:
    a = int(input("Nhập hệ số thứ nhất: "))
    b = int(input("Nhập hệ số thứ hai: "))
    c = int(input("Nhập hệ số thứ ba: "))
    giaipt.pt_bac_hai(a, b, c)
else:
    print("Chức năng chưa được cập nhật. Vui lòng thử lại sau!")