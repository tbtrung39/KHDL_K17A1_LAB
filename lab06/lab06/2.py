n = int(input("Nhập số phần tử của danh sách: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Nhập phần tử thứ {i+1}: ")))
arr_sắp_xếp = sorted(arr, reverse=True)
lớn_thứ_hai = arr_sắp_xếp[1]
vị_trí_lớn_thứ_hai = arr.index(lớn_thứ_hai)
print(f"Phần tử lớn thứ hai của danh sách là {lớn_thứ_hai} tại vị trí {vị_trí_lớn_thứ_hai}")
số_lượng_dương_liên_tiếp = 0
dương_liên_tiếp_hiện_tại = 0
for số in arr:
    if số > 0:
        dương_liên_tiếp_hiện_tại += 1
        số_lượng_dương_liên_tiếp = max(số_lượng_dương_liên_tiếp, dương_liên_tiếp_hiện_tại)
    else:
        dương_liên_tiếp_hiện_tại = 0
print(f"Số lượng các số dương liên tiếp nhiều nhất là {số_lượng_dương_liên_tiếp}")
tổng_max = 0
tổng_hiện_tại = 0
for số in arr:
    if số > 0:
        tổng_hiện_tại += số
        tổng_max = max(tổng_max, tổng_hiện_tại)
    else:
        tổng_hiện_tại = 0
print(f"Tổng của dãy số dương liên tiếp lớn nhất là {tổng_max}")
