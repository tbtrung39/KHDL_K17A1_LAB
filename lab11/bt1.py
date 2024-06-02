def doc_va_tinh_tong_so_le(ten_tap_tin):
    tong_so_le = 0
    with open('lab11/dayso.dat','r') as file:
        for i in file:
            cac_so = map(int, i.split())
            tong_so_le += sum(so for so in cac_so if so % 2 != 0)
        return tong_so_le
ten_tap_tin = 'dayso.dat'
tong_le = doc_va_tinh_tong_so_le(ten_tap_tin)
if tong_le is not None:
    print(f"Tổng các số lẻ trong tệp là: {tong_le}")