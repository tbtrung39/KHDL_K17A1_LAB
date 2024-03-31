# Số mol NaOH ban đầu
mol_NaOH = y * 100 / 1000

# Số mol HCl thêm vào
mol_HCl = z * 100 / 1000

# Số mol NaOH còn sau phản ứng
mol_NaOH_after_rxn = mol_NaOH - mol_HCl

# Số mol Al2O3
mol_Al2O3 = x / 101.96

# Số mol NaAlO2 tạo ra
mol_NaAlO2 = mol_Al2O3

if mol_NaAlO2 > 2 * mol_NaOH_after_rxn:
    print("Sau phản ứng có kết tủa.")
else:
    print("Sau phản ứng không có kết tủa.")