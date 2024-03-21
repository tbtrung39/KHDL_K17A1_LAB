a = float(input("Nhập số lượng (gram) Al2O3: "))
b = float(input("Nhập nồng độ (mol/lit) dung dịch NaOH: "))
c = float(input("Nhập nồng độ (mol/lit) dung dịch HCl: "))
so_mol_NaOH = b * 0.1  
so_mol_HCl = c * 0.1  
so_mol_NaOH_con_lai = b * 0.1 - so_mol_HCl
so_mol_Al2O3 = so_mol_NaOH / 2  
if so_mol_NaOH_con_lai < so_mol_Al2O3:
    print("Sau phản ứng có kết tủa.")
else:
    print("Sau phản ứng không có kết tủa.")