import sys
sys.path.append("lab10\packages")
import packages
n = int(input("n: "))
print("hệ nhị phân: ", packages.he_nhi_phan(n))
print("hệ bát phân: ", packages.he_bat_phan(n))
print("hệ 16: ", packages.he_thap_luc_phan(n))