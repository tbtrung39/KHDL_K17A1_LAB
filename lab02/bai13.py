x = float(input("Nhập lượng Al2O3 (gam): "))
y = float(input("Nhập nồng độ NaOH (mol/l): "))
z = float(input("Nhập nồng độ HCl (mol/l): "))

# Tính số mol của Al2O3, NaOH và HCl
M_Al2O3 = 101.96  
V_NaOH = 100  
V_HCl = 100  

mol_Al2O3 = x / M_Al2O3
mol_NaOH = y * V_NaOH / 1000  
mol_HCl = z * V_HCl / 1000  

# Tính số mol của Al3+ trong dung dịch ban đầu và sau phản ứng với NaOH
mol_Al3_plus = 2 * mol_Al2O3  # Mỗi phân tử Al2O3 tạo ra 2 Al3+
mol_Al3_plus_final = mol_Al3_plus - mol_NaOH  # Al(OH)3 tan hết

# Kiểm tra xem có kết tủa Al(OH)3 hay không
if mol_Al3_plus_final > 0:
    print("Sau phản ứng có kết tủa Al(OH)3.")
else:
    print("Sau phản ứng không có kết tủa Al(OH)3.")
