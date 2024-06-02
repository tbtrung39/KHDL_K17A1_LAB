def doc_du_lieu_tap_tin(ten_tap_tin):
    du_lieu = []
    with open(ten_tap_tin, 'r') as file:
        for line in file:
            du_lieu.append(line.strip().split())
    return du_lieu

def ghep_phan_tin(sbd_phach, sbd_ten, phieu_diem):
    danh_sach_thi_sinh = []
    
    # Tạo từ điển phách -> SBD
    phach_sbd = {int(p[1]): int(p[0]) for p in sbd_phach}
    
    # Tạo từ điển phách -> tên
    phach_ten = {int(t[0]): ' '.join(t[1:]) for t in sbd_ten}
    
    # Tạo danh sách thí sinh với thông tin đầy đủ
    for p in phieu_diem:
        phach = int(p[0])
        diem = float(p[1])
        sbd = phach_sbd[phach]
        ten = phach_ten[phach]
        danh_sach_thi_sinh.append((sbd, ten, diem))
    
    return danh_sach_thi_sinh

def sap_xep_va_ghi_tap_tin(danh_sach_thi_sinh, ten_tap_tin_ra):
    # Sắp xếp danh sách thí sinh theo điểm giảm dần
    danh_sach_thi_sinh.sort(key=lambda x: x[2], reverse=True)
    
    # Ghi kết quả vào tệp
    with open(ten_tap_tin_ra, 'w') as file:
        for thi_sinh in danh_sach_thi_sinh:
            file.write(f"{thi_sinh[0]} {thi_sinh[1]} {thi_sinh[2]}\n")

# Đọc dữ liệu từ các tệp
sbd_phach = doc_du_lieu_tap_tin('Sbd_Ph.dat')
sbd_ten = doc_du_lieu_tap_tin('SBD_Ten.txt')
phieu_diem = doc_du_lieu_tap_tin('Phieu_Diem.txt')

# Ghép thông tin từ các tệp
danh_sach_thi_sinh = ghep_phan_tin(sbd_phach, sbd_ten, phieu_diem)

# Sắp xếp và ghi kết quả vào tệp Ketqua.txt
sap_xep_va_ghi_tap_tin(danh_sach_thi_sinh, 'Ketqua.txt')
