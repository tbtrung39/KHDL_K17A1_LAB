import re

def loai_bo_ky_tu_khong_hop_le(chuoi):
    chuoi_loai_bo = re.sub(r'[^0-9ABCDEF.]', '', chuoi.upper())
    print("Chuỗi sau khi loại bỏ ký tự không hợp lệ là:", chuoi_loai_bo)

def co_so_cua_chuoi(so):
    try:
        int(so, 2)
        print("Chuỗi", so, "là biểu diễn cơ số 2.")
    except ValueError:
        try:
            int(so, 8)
            print("Chuỗi", so, "là biểu diễn cơ số 8.")
        except ValueError:
            try:
                int(so, 10)
                print("Chuỗi", so, "là biểu diễn cơ số 10.")
            except ValueError:
                try:
                    int(so, 16)
                    print("Chuỗi", so, "là biểu diễn cơ số 16.")
                except ValueError:
                    print("Chuỗi", so, "không phải là biểu diễn của bất kỳ cơ số nào.")

def chuyen_doi_2_sang_10(chuoi):
    return int(chuoi, 2)

def chuyen_doi_8_sang_10(chuoi):
    return int(chuoi, 8)

def chuyen_doi_16_sang_10(chuoi):
    return int(chuoi, 16)