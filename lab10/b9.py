import sys
sys.path.append("lab10\packages")
import packages
dss = []
ds = packages.nhap_hang_hoa()
print(ds)
dss.append(ds)
print(packages.sap_xep_theo_thue(dss))