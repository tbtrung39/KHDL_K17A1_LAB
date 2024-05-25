def nhap_matran(kich_thuoc):
    matran = []
    print("Nhập dữ liệu cho ma trận:")
    for i in range(kich_thuoc):
        hang = []
        for j in range(kich_thuoc):
            hang.append(int(input(f"Nhập phần tử [{i+1}][{j+1}]: ")))
        matran.append(hang)
    return matran

def in_matran(matran):
    print("Ma trận:")
    for hang in matran:
        print(hang)

def chuyen_vi(matran, kich_thuoc):
    return [[matran[j][i] for j in range(kich_thuoc)] for i in range(kich_thuoc)]

def kiem_tra_doi_xung(matran, kich_thuoc):
    for i in range(kich_thuoc):
        for j in range(i, kich_thuoc):
            if matran[i][j] != matran[j][i]:
                return False
    return True