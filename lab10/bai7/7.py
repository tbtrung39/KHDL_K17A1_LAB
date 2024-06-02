import module7
def main():
    # Sinh ngẫu nhiên một dãy số
    day_so = module7.sinh_day_so()
    
    # Hiển thị dãy số
    module7.hien_thi_day_so(day_so)
    
    # Liệt kê và hiển thị các số chia hết cho 7
    module7.so_chia_het_cho_7(day_so)
    
    # Tính tổng các số lẻ
    module7.tong_so_le(day_so)
    
    # Kiểm tra và hiển thị các số chính phương
    module7.so_chinh_phuong(day_so)

if __name__ == "__main__":
    main()
