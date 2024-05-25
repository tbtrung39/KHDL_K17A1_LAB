import sys
sys.path.append("lab10\packages")
import packages
a = int(input("a: "))
b = int(input("b: "))
print("ucnl: ", packages.ucln(a,b))
print("bcnn: ", packages.bcnn(a,b))