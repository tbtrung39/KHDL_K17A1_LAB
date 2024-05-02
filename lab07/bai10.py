so_nguyen_m = input("Nhập số tự nhiên m: ")
so_nguyen_n = input("Nhập số tự nhiên n: ")

chu_so_m = set(so_nguyen_m)
chu_so_n = set(so_nguyen_n)

chu_so_chung = chu_so_m & chu_so_n
cac_chu_so_chung = list(chu_so_chung)

tong_cac_chu_so_chung = 0
for chu_so in cac_chu_so_chung:
    tong_cac_chu_so_chung += int(chu_so)

print("Tổng các chữ số chung của m và n là:", tong_cac_chu_so_chung)
