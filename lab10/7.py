import sys

sys.path.append("lab10/packages")

import package

n = int(input("Nhập vào một số nguyên: "))

print(f"Hệ nhị phân của {n} là {package.he_nhi_phan(n)}")
print(f"Hệ bát phân của {n} là {package.he_bat_phan(n)}")
print(f"Hệ thập lục phân của {n} là {package.he_thap_luc_phan(n)}")