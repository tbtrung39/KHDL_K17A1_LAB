import doicoso1
n = doicoso1.nhap_so()
print(f"Số vừa nhập: {n}")
# Chuyển đổi số đã nhập sang hệ nhị phân 
nhi_phan = doicoso1.doi_sang_nhi_phan(n)
print(f"Số {n} trng hệ nhị phân là: {nhi_phan}")
# Chuyển đổi số đã nhập sang hệ cơ số 8 
bat_phan = doicoso1.doi_sang_bat_phan(n)
print(f"Số {n} trong hệ bát phân là: {bat_phan}")
# Chuyển đổi số đã nhập sang hệ cơ số 16 
thap_luc_phan = doicoso1.doi_sang_thap_luc_phan(n)
print(f"Số {n} trong hệ thập lục phân là: {thap_luc_phan}")