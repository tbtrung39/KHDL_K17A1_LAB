from pk_4 import modul

a = int(input("Nhập giá trị a: "))
b = int(input("Nhập giá trị b: "))

ket_qua_bac_nhat = modul.giai_phuong_trinh_bac_nhat(a, b)
ket_qua_bac_hai = modul.giai_phuong_trinh_bac_hai(a, b, 0)  # Giả sử c = 0

print("Kết quả giải phương trình bậc nhất:", ket_qua_bac_nhat)
print("Kết quả giải phương trình bậc hai:", ket_qua_bac_hai)
