def doc_du_lieu_Sbd_Ph(ten_tap_tin):
    sbd_phach = {}
    with open('lab11/Sbd_Ph.dat', 'r') as tap_tin:
        for line in tap_tin:
            sbd = int(line[:line.index(' ')])
            phach = int(line[line.index(' ')+1:])
            sbd_phach[sbd] = phach
    return sbd_phach

def doc_du_lieu_Sbd_Ten(ten_tap_tin):
    sbd_ten = {}
    with open('lab11/Sbd_Ten.txt', 'r') as tap_tin:
        for line in tap_tin:
            sbd = int(line[:line.index(' ')])
            ten = line[line.index(' ')+1:].rstrip('\n')
            sbd_ten[sbd] = ten
    return sbd_ten

def doc_du_lieu_Phieu_Diem(ten_tap_tin):
    phach_diem = {}
    with open('lab11/Phieu_Diem.txt', 'r') as tap_tin:
        for line in tap_tin:
            phach = int(line[:line.index(' ')])
            diem = int(line[line.index(' ')+1:])
            phach_diem[phach] = diem
    return phach_diem

def ghep_phach_sbd(sbd_phach, sbd_ten, phach_diem):
    thong_tin = []
    for sbd, phach in sbd_phach.items():
        if sbd in sbd_ten and phach in phach_diem:
            thong_tin.append((sbd, sbd_ten[sbd], phach_diem[phach]))
    return thong_tin

def sap_xep_va_ghi_ket_qua(thong_tin, ten_tap_tin):
    with open('lab11/Ketqua.txt', 'w') as tap_tin:
        for sbd, ten, diem in sorted(thong_tin, key=lambda x: x[2], reverse=True):
            tap_tin.write(f"{sbd} {ten} {diem}\n")

sbd_phach = doc_du_lieu_Sbd_Ph("Sbd_Ph.dat")
sbd_ten = doc_du_lieu_Sbd_Ten("Sbd_Ten.txt")
phach_diem = doc_du_lieu_Phieu_Diem("Phieu_Diem.txt")

thong_tin = ghep_phach_sbd(sbd_phach, sbd_ten, phach_diem)

sap_xep_va_ghi_ket_qua(thong_tin, "Ketqua.txt")
