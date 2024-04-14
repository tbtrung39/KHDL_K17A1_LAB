print(" ___________________")
print("|NHAT KY GIAO DICH! |")
print("|Gui tien nhap D    |")
print("|Rut tien nhap W    |")
print("|___________________|")

nhat_ky_giao_dich=input("Nhap chuc nang: ").strip().split("\n")
so_du = 0
for giao_dich in nhat_ky_giao_dich:
    hanh_dong,so_tien = giao_dich.split()
    so_tien = int(so_tien)
    if hanh_dong == "D":
        so_du+= so_tien
    elif hanh_dong == "W":
        so_du -= so_tien
    else:
        print("Nhap vao khong hop le!")
print(so_du)
