def loai_bo_ky_tu_khong_hop_le(chuoi):
    ky_tu_hop_le = set("0123456789ABCDEF")
    chuoi_loai_bo = ''.join(filter(lambda x: x.upper() in ky_tu_hop_le, chuoi))
    print("Chuỗi sau khi loại bỏ các ký tự không hợp lệ:", chuoi_loai_bo)
def bieu_dien_co_so(chuoi):
    co_so = None
    if all(char in "01" for char in chuoi):
        co_so = 2
    elif all(char in "01234567" for char in chuoi):
        co_so = 8
    elif all(char.isdigit() for char in chuoi):
        co_so = 10
    elif all(char.upper() in "0123456789ABCDEF" for char in chuoi):
        co_so = 16

    if co_so is not None:
        print("Chuỗi", chuoi, "là biểu diễn cơ số", co_so)
    else:
        print("Không thể xác định cơ số của chuỗi", chuoi)
def chuyen_doi_co_so(chuoi, co_so_cu, co_so_moi):
    chuoi_so = chuoi.upper()
    chuoi_hop_le = set("0123456789ABCDEF")
    if all(char in chuoi_hop_le for char in chuoi_so):
        try:
            so_nguyen = int(chuoi_so, co_so_cu)
            if co_so_moi == 2:
                chuoi_moi = bin(so_nguyen)
            elif co_so_moi == 8:
                chuoi_moi = oct(so_nguyen)
            elif co_so_moi == 10:
                chuoi_moi = str(so_nguyen)
            elif co_so_moi == 16:
                chuoi_moi = hex(so_nguyen)
            print("Chuỗi số", chuoi, "trong cơ số", co_so_cu, "chuyển sang cơ số", co_so_moi, "là:", chuoi_moi)
        except ValueError:
            print("Không thể chuyển đổi chuỗi số", chuoi, "từ cơ số", co_so_cu, "sang cơ số", co_so_moi)
    else:
        print("Chuỗi", chuoi, "không hợp lệ trong cơ số", co_so_cu)
