# Module: doicoso2.py

def loai_bo_ky_tu(s):
    """Nhập vào một chuỗi ký tự, loại bỏ tất cả các ký tự không thuộc vào tập hợp các ký tự {0-9, A-F}."""
    tap_hop_ky_tu = set('0123456789ABCDEF')
    ket_qua = ''.join([ky_tu for ky_tu in s.upper() if ky_tu in tap_hop_ky_tu])
    print(f"Chuỗi sau khi loại bỏ các ký tự không hợp lệ: {ket_qua}")
    return ket_qua

def xac_dinh_he_co_so(s):
    """Cho biết một chuỗi số cho trước là biểu diễn cơ số mấy."""
    s = s.upper()
    if all(ky_tu in '01' for ky_tu in s):
        return 2
    elif all(ky_tu in '01234567' for ky_tu in s):
        return 8
    elif all(ky_tu in '0123456789ABCDEF' for ky_tu in s):
        return 16
    else:
        return "Chuỗi không thuộc các hệ cơ số 2, 8, hoặc 16."

def chuyen_doi_tu_co_so_2_sang_10(s):
    """Chuyển đổi một chuỗi số từ cơ số 2 sang cơ số 10."""
    try:
        gia_tri = int(s, 2)
        print(f"Chuỗi {s} trong hệ cơ số 2 chuyển sang hệ cơ số 10 là: {gia_tri}")
        return gia_tri
    except ValueError:
        print("Chuỗi không hợp lệ trong hệ cơ số 2.")
        return None

def chuyen_doi_tu_co_so_8_sang_10(s):
    """Chuyển đổi một chuỗi số từ cơ số 8 sang cơ số 10."""
    try:
        gia_tri = int(s, 8)
        print(f"Chuỗi {s} trong hệ cơ số 8 chuyển sang hệ cơ số 10 là: {gia_tri}")
        return gia_tri
    except ValueError:
        print("Chuỗi không hợp lệ trong hệ cơ số 8.")
        return None

def chuyen_doi_tu_co_so_16_sang_10(s):
    """Chuyển đổi một chuỗi số từ cơ số 16 sang cơ số 10."""
    try:
        gia_tri = int(s, 16)
        print(f"Chuỗi {s} trong hệ cơ số 16 chuyển sang hệ cơ số 10 là: {gia_tri}")
        return gia_tri
    except ValueError:
        print("Chuỗi không hợp lệ trong hệ cơ số 16.")
        return None