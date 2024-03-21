def tinh_dien_tich_xung_quanh(r, h):
    # Diện tích xung quanh
    dien_tich_xung_quanh = 2 * 3.14 * r * h
    return dien_tich_xung_quanh

def tinh_dien_tich_toan_phan(r, h):
    # Diện tích toàn phần
    dien_tich_toan_phan = 2 * 3.14 * r * (r + h)
    return dien_tich_toan_phan

def tinh_the_tich(r, h):
    # Thể tích
    the_tich = 3.14 * r**2 * h
    return the_tich

def main():
    # Nhập bán kính và chiều cao từ bàn phím
    r = float(input("Nhập bán kính của khối trụ: "))
    h = float(input("Nhập chiều cao của khối trụ: "))
    
    # Tính diện tích xung quanh
    dien_tich_xung_quanh = tinh_dien_tich_xung_quanh(r, h)
    
    # Tính diện tích toàn phần
    dien_tich_toan_phan = tinh_dien_tich_toan_phan(r, h)
    
    # Tính thể tích
    the_tich = tinh_the_tich(r, h)
    
    # In kết quả
    print("Diện tích xung quanh của khối trụ là:", round(dien_tich_xung_quanh, 2))
    print("Diện tích toàn phần của khối trụ là:", round(dien_tich_toan_phan, 2))
    print("Thể tích của khối trụ là:", round(the_tich, 2))

if __name__ == "__main__":
    main()