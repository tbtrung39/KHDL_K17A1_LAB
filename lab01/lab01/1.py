ban_kinh = float(input("nhap ban kinh"))
chieu_cao=float(input("nhap chieu cao"))
dt_xung_quanh=2*3.14*ban_kinh*chieu_cao
dt_toan_phan=2*3.14*ban_kinh*chieu_cao+2*3.14*(ban_kinh**2)
V=3.14*(ban_kinh**2)*chieu_cao
print(f"V={V:.2f}, dt_xung_quanh={dt_xung_quanh:.2f},dt_toan_phan={dt_toan_phan:.2f}")