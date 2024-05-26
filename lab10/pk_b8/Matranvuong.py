def nhap_ma_tran(n):
    """Nhập dữ liệu vào ma trận NxN từ bàn phím"""
    ma_tran = []
    for i in range(n):
        hang = []
        print(f"Nhập các phần tử của hàng thứ {i + 1}:")
        for j in range(n):
            while True:
                try:
                    phan_tu = int(input(f"Phần tử [{i + 1}][{j + 1}]: "))
                    hang.append(phan_tu)
                    break
                except ValueError:
                    print("Giá trị nhập không hợp lệ. Vui lòng nhập một số nguyên.")
        ma_tran.append(hang)
    return ma_tran

def in_ma_tran(ma_tran):
    """In ma trận ra màn hình theo định dạng truyền thống"""
    for hang in ma_tran:
        print(' '.join(map(str, hang)))

def tinh_ma_tran_chuyen_vi(ma_tran):
    """Tính ma trận chuyển vị"""
    n = len(ma_tran)
    chuyen_vi = [[ma_tran[j][i] for j in range(n)] for i in range(n)]
    return chuyen_vi

def kiem_tra_doi_xung(ma_tran):
    """Kiểm tra ma trận có đối xứng hay không"""
    n = len(ma_tran)
    for i in range(n):
        for j in range(i, n):
            if ma_tran[i][j] != ma_tran[j][i]:
                return False
    return True
