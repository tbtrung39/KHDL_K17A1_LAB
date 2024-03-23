x = float(input("Nhập số gam Al2O3: "))
y = float(input("Nhập nồng độ NaOH yM: "))
z = float(input("Nhập nồng độ HCl zM: "))

mol_NaOH = y * 100 / 1000

mol_HCl = z * 100 / 1000

mol_Al2O3 = x / 101.96

mol_NaOH_du = mol_NaOH - 2 * mol_Al2O3

mol_HCl_du = mol_HCl - 6 * mol_Al2O3

if mol_NaOH_du < 0 or mol_HCl_du < 0:
    print("Có kết tủa sau phản ứng.")
else:
    print("Không có kết tủa sau phản ứng.")