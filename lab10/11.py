import sys
sys.path.append("lab10\doicoso")
import packages
n = int(input("n: "))
s = input("nhập s: ")
print("hệ nhị phân: ", packages.he_nhi_phan(n))
print("hệ bát phân: ", packages.he_bat_phan(n))
print("hệ 16: ", packages.he_thap_luc_phan(n))
print("hệ", packages.kiem_tra(s))
print("chuyển đổi: ", packages.mot(s), packages.hai(s) , packages.ba(s))