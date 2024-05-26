import sys
sys.path.append("lab10\packages")
import packages
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
print(packages.is_TamGiac(a,b,c))
print(packages.ChuviTamGiac(a,b,c))
print(packages.S_TamGiac(a,b,c))