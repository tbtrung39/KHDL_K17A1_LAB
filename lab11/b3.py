def doc_cac_so_tu_tap_tin(ten_tap_tin):
    with open('lab11/f_in.dat', 'r') as tap_tin:
        cac_so = []
        so_hien_tai = ''
        ky_tu = tap_tin.read(1)
        while ky_tu:
            if ky_tu != ' ' and ky_tu != '\n': 
                so_hien_tai += ky_tu
            else:
                if so_hien_tai: 
                    cac_so.append(int(so_hien_tai)) 
                    so_hien_tai = '' 
            ky_tu = tap_tin.read(1)
        if so_hien_tai:
            cac_so.append(int(so_hien_tai))
    return cac_so

def tim_cac_phan_tu_cuc_tri(cac_so):
    cac_phan_tu_cuc_tri = []
    for i in range(1, len(cac_so) - 1):
        if (cac_so[i-1] < cac_so[i] > cac_so[i+1]) or (cac_so[i-1] > cac_so[i] < cac_so[i+1]):
            cac_phan_tu_cuc_tri.append(cac_so[i])
    return cac_phan_tu_cuc_tri

def ghi_cac_phan_tu_cuc_tri_vao_tap_tin(ten_tap_tin, cac_phan_tu_cuc_tri):
    with open('lab11/f_out.dat', 'w') as tap_tin:
        tap_tin.write(f"{len(cac_phan_tu_cuc_tri)}\n")
        tap_tin.write(' '.join(map(str, cac_phan_tu_cuc_tri)))

ten_tap_tin_vao = 'f_in.dat'
ten_tap_tin_ra = 'f_out.dat'

cac_so = doc_cac_so_tu_tap_tin(ten_tap_tin_vao)

if cac_so:
    cac_phan_tu_cuc_tri = tim_cac_phan_tu_cuc_tri(cac_so)

    ghi_cac_phan_tu_cuc_tri_vao_tap_tin(ten_tap_tin_ra, cac_phan_tu_cuc_tri)

    print(f"Đã tìm thấy {len(cac_phan_tu_cuc_tri)} phần tử cực trị và ghi vào tệp {ten_tap_tin_ra}.")
else:
    print("Không có số nào để xử lý.")
