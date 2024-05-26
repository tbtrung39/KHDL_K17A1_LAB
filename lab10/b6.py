from pk_b6 import doicoso2
def main():
    chuoi_nhap = input("Nhập vào một chuỗi ký tự: ")
    
    chuoi_sach = doicoso2.loai_bo_ky_tu_khong_hop_le(chuoi_nhap)
    print("Chuỗi sau khi loại bỏ các ký tự không hợp lệ:", chuoi_sach)
    
    co_so = doicoso2.phat_hien_co_so(chuoi_sach)
    if co_so == -1:
        print("Không xác định được cơ số của chuỗi.")
    else:
        print(f"Chuỗi thuộc cơ số: {co_so}")
    
    if co_so == 2:
        ket_qua = doicoso2.doi_co_so_2_sang_10(chuoi_sach)
        print(f"Chuỗi cơ số 2 chuyển sang cơ số 10 là: {ket_qua}")
    elif co_so == 8:
        ket_qua = doicoso2.doi_co_so_8_sang_10(chuoi_sach)
        print(f"Chuỗi cơ số 8 chuyển sang cơ số 10 là: {ket_qua}")
    elif co_so == 16:
        ket_qua = doicoso2.doi_co_so_16_sang_10(chuoi_sach)
        print(f"Chuỗi cơ số 16 chuyển sang cơ số 10 là: {ket_qua}")
    else:
        print("Chuyển đổi không khả dụng cho cơ số này.")

if __name__ == "__main__":
    main()
