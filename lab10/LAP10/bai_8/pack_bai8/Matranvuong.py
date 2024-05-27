def nhap_ma_tran(n):
    print("Nhập ma trận vuông", n, "x", n)
    ma_tran = []
    for i in range(n):
        hang = [int(x) for x in input().split()]
        ma_tran.append(hang)
    return ma_tran

def in_ma_tran(ma_tran):
    print("Ma trận vừa nhập là:")
    for hang in ma_tran:
        print(" ".join(map(str, hang)))

def ma_tran_chuyen_vi(ma_tran):
    return [[ma_tran[j][i] for j in range(len(ma_tran))] for i in range(len(ma_tran))]

def kiem_tra_ma_tran_doi_xung(ma_tran):
    return ma_tran == ma_tran_chuyen_vi(ma_tran)