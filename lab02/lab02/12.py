x = float(input("Nhập số gam Al2O3: "))
y = float(input("Nhập nồng độ NaOH (yM): "))
z = float(input("Nhập nồng độ HCl (zM): "))

# Tính số mol của các chất
mol_Al2O3 = x / 101.96  # Khối lượng mol của Al2O3
vol_NaOH = 0.1 * y      # Thể tích NaOH sau phản ứng (100ml)
vol_HCl = 0.1 * z       # Thể tích HCl sau phản ứng (100ml)

# Số mol của NaOH và HCl trước phản ứng
mol_NaOH_trc = y * 0.1
mol_HCl_trc = z * 0.1

# Số mol của NaOH và HCl sau phản ứng
mol_NaOH_sau = mol_NaOH_trc - mol_Al2O3 / 6
mol_HCl_sau = mol_HCl_trc - mol_Al2O3 / 6

# Kiểm tra xem có kết tủa hay không
if mol_NaOH_sau < 0 or mol_HCl_sau < 0:
    print("Sau phản ứng có kết tủa.")
else:
    print("Sau phản ứng không có kết tủa.")