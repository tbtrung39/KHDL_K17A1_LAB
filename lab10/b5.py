import sys
sys.path.append("lab10/packages")
import packages
n = int(input("Nhập vào một số nguyên: "))
print(f"Hệ nhị phân của {n} là {packages.he_nhi_phan(n)}")
print(f"Hệ bát phân của {n} là {packages.he_bat_phan(n)}")
print(f"Hệ thập lục phân của {n} là {packages.he_thap_luc_phan(n)}")
