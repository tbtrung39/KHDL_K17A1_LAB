from pk_b7 import xulydayso

def main():
    day_so = xulydayso.sinh_ngau_nhien_day_so()
    print("Dãy số ngẫu nhiên:", day_so)
    
    so_nguyen_to_chia_het_cho_7 = xulydayso.liet_ke_nguyen_to_chia_het_cho_7(day_so)
    print("Các số nguyên tố chia hết cho 7:", so_nguyen_to_chia_het_cho_7)
    
    tong_so_le = xulydayso.tinh_tong_so_le(day_so)
    print("Tổng các số lẻ trong dãy:", tong_so_le)
    
    so_chinh_phuong = xulydayso.kiem_tra_va_hien_thi_so_chinh_phuong(day_so)
    if so_chinh_phuong:
        print("Các số chính phương trong dãy:", so_chinh_phuong)
    else:
        print("Không có số chính phương nào trong dãy.")

if __name__ == "__main__":
    main()
