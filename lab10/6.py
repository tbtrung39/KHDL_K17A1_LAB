import sys
sys.path.append("lab10\packages")
import packages
s = input("nhập s: ")
print("hệ", packages.kiem_tra(s))
print("chuyển đổi: ", packages.mot(s), packages.hai(s) , packages.ba(s))