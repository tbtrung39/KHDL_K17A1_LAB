# File sử dụng module: main.py

from package_6 import doicoso2

def main():
    s = input("Nhập vào một chuỗi ký tự: ")
    
    chuoi_ket_qua = doicoso2.loai_bo_ky_tu(s)
    
    he_co_so = doicoso2.xac_dinh_he_co_so(chuoi_ket_qua)
    print(f"Chuỗi {chuoi_ket_qua} thuộc hệ cơ số: {he_co_so}")

    if he_co_so == 2:
        doicoso2.chuyen_doi_tu_co_so_2_sang_10(chuoi_ket_qua)
    elif he_co_so == 8:
        doicoso2.chuyen_doi_tu_co_so_8_sang_10(chuoi_ket_qua)
    elif he_co_so == 16:
        doicoso2.chuyen_doi_tu_co_so_16_sang_10(chuoi_ket_qua)
    else:
        print("Không thể chuyển đổi chuỗi không hợp lệ.")

if __name__ == "__main__":
    main()