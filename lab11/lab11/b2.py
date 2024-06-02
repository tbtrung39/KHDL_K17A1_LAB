def doc_va_sap_xep_tap_tin(ten_tap_tin_vao, ten_tap_tin_ra):
    with open(ten_tap_tin_vao, 'r') as file:
        noi_dung = file.read()
        cac_so = list(map(int, noi_dung.split()))
        cac_so.sort()
        noi_dung_da_sap_xep = ' '.join(map(str, cac_so))
        with open(ten_tap_tin_ra, 'w') as file_out:
            file_out.write(noi_dung_da_sap_xep)
            print(f"Dữ liệu đã được sắp xếp và ghi vào tệp {ten_tap_tin_ra}.")

# Tên đầu vào và đầu ra của tệp
ten_tap_tin_vao = 'Inp.txt'
ten_tap_tin_ra = 'out.dat'

# Gọi hàm để xử lý file
doc_va_sap_xep_tap_tin(ten_tap_tin_vao, ten_tap_tin_ra)
