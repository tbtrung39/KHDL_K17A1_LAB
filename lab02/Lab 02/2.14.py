x = float(input("Nhập số lượng Al2O3 (gam): "))
y = float(input("Nhập nồng độ NaOH (mol/l): "))
z = float(input("Nhập nồng độ HCl (mol/l): "))
Al2O3_mol = x / 160
NaOH_mol = y * 0.1
HCl_mol = z * 0.1

if Al2O3_mol > 2 * NaOH_mol: #Al2O3 dư
    Al2O3_mol = Al2O3_mol - 2 * NaOH_mol
    NaOH_mol = 0


    if Al2O3_mol > 6 * HCl_mol:
        print("Có kết tủa Al2O3.")
    else:
        print("Không có kết tủa.")
else:
    print("Không có kết tủa.")