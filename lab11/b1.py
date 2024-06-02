def doc_cac_so_tu_tap_tin(ten_tap_tin):
    cac_so = []
    so_hien_tai = ''
    with open('lab11/dayso.dat', 'r') as tap_tin:
        while True:
            ky_tu = tap_tin.read(1)
            if not ky_tu:
                if so_hien_tai:
                    cac_so.append(int(so_hien_tai))
                break
            if ky_tu.isdigit():
                so_hien_tai += ky_tu
            else:
                if so_hien_tai:
                    cac_so.append(int(so_hien_tai))
                    so_hien_tai = ''
    return cac_so

def tinh_tong_cac_so_le(cac_so):
    return sum(so for so in cac_so if so % 2 != 0)

ten_tap_tin = 'dayso.dat'
cac_so = doc_cac_so_tu_tap_tin(ten_tap_tin)

tong_so_le = tinh_tong_cac_so_le(cac_so)

print(f"Tổng các số lẻ trong dãy là: {tong_so_le}")
