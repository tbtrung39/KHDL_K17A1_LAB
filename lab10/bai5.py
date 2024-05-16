import sys
sys.path.append("lab10\package_5")

import package_5

n=package_5.nhap_so()
print(f'chuyen {n} sang he nhi phan:')
print(package_5.chuyen_sang_he_nhi_phan(n))
print(f'chuyen {n} sang he co so 8:')
print(package_5.chuyen_sang_he_bat_phan(n))
print(f'chuyen {n} sang he co so 16:')
print(package_5.chuyen_sang_he_16(n))