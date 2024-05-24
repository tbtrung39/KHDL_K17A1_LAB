# Module: Matranvuong.py

def nhap_ma_tran(n):
    """Nhập dữ liệu vào ma trận NxN."""
    ma_tran = []
    print(f"Nhập ma trận kích thước {n}x{n}:")
    for i in range(n):
        hang = list(map(int, input(f"Nhập dòng {i + 1} (cách nhau bằng khoảng trắng): ").split()))
        if len(hang) != n:
            raise ValueError(f"Mỗi dòng phải có đúng {n} phần tử.")
        ma_tran.append(hang)
    return ma_tran

def in_ma_tran(ma_tran):
    """In ma trận ra màn hình theo định dạng truyền thống."""
    print("Ma trận:")
    for hang in ma_tran:
        print(" ".join(map(str, hang)))

def ma_tran_chuyen_vi(ma_tran):
    """Tính ma trận chuyển vị và in kết quả ra màn hình."""
    n = len(ma_tran)
    ma_tran_cv = [[ma_tran[j][i] for j in range(n)] for i in range(n)]
    print("Ma trận chuyển vị:")
    in_ma_tran(ma_tran_cv)
    return ma_tran_cv

def kiem_tra_doi_xung(ma_tran):
    """Kiểm tra ma trận có đối xứng không."""
    n = len(ma_tran)
    for i in range(n):
        for j in range(i, n):
            if ma_tran[i][j] != ma_tran[j][i]:
                return False
    return True