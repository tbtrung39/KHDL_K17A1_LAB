sinh_vien = {}
n = int(input("nhap so luong thi sinh: "))

for i in range(n):
    so_bao_danh = input("nhap so bao danh: ")
    ten = input("nhap ho va ten: ")
    diem = float(input("nhap diem: "))
    sinh_vien[so_bao_danh] = {"ten": ten, "diem": diem}

so_bao_danh_can_tim = input("nhap so bao danh can tim kiem: ")

if so_bao_danh_can_tim in sinh_vien:
    print("Tên:", sinh_vien[so_bao_danh_can_tim]["ten"])
    print("Điểm:", sinh_vien[so_bao_danh_can_tim]["diem"])
else:
    print("Thí sinh không tồn tại.")    
    ten_moi = input("nhap ten cua thi sinh moi: ")
    diem_moi = float(input("nhap diem cua thi sinh moi: "))
    sinh_vien[so_bao_danh_can_tim] = {"ten": ten_moi, "diem": diem_moi}
    print("nhap thong tin cua thi sinh moi da thanh cong!!!")
print("Thông tin của tất cả thí sinh:")