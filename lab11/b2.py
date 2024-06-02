def doc_cac_so_tu_tap_tin(ten_tap_tin):
    with open('lab11/Inp.txt', 'r') as tap_tin:
        noi_dung = tap_tin.read().strip()
        cac_so = list(map(int, noi_dung.split()))
    return cac_so

def ghi_cac_so_vao_tap_tin(ten_tap_tin, cac_so):
    with open('lab11/out.dat', 'w') as tap_tin:
        tap_tin.write(' '.join(map(str, cac_so)))

ten_tap_tin_vao = 'lab11/Inp.txt'
cac_so = doc_cac_so_tu_tap_tin(ten_tap_tin_vao)

cac_so.sort()

ten_tap_tin_ra = 'lab11/out.dat'
ghi_cac_so_vao_tap_tin(ten_tap_tin_ra, cac_so)

print(f"Các số đã được sắp xếp và ghi vào tệp {ten_tap_tin_ra}")
