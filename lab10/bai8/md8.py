def nhap_matran_vuong(kich_thuoc):
    matran = []
    print("Nhập dữ liệu cho ma trận:")
    for i in range(kich_thuoc):
        hang = []
        for j in range(kich_thuoc):
            gia_tri = int(input(f"Nhập phần tử [{i}][{j}]: "))
            hang.append(gia_tri)
        matran.append(hang)
    return matran

def in_matran_vuong(matran):
    print("Ma trận:")
    for hang in matran:
        print(" ".join(map(str, hang)))

def chuyen_vi_matran_vuong(matran):
    matran_chuyen_vi = []
    for j in range(len(matran)):
        hang_chuyen_vi = []
        for i in range(len(matran)):
            hang_chuyen_vi.append(matran[i][j])
        matran_chuyen_vi.append(hang_chuyen_vi)
    return matran_chuyen_vi

def kiem_tra_doi_xung(matran):
    for i in range(len(matran)):
        for j in range(i, len(matran)):
            if matran[i][j] != matran[j][i]:
                return False
    return True
