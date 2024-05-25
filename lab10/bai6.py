import sys
sys.path.append("lab10\package_6")

import package_6

chuoi_hop_le = package_6.nhap_va_loc_chuoi()
co_so = package_6.xac_dinh_co_so(chuoi_hop_le)

if co_so == 2:
    package_6.chuyen_co_so_2_sang_co_so_10(chuoi_hop_le)
elif co_so == 8:
    package_6.chuyen_co_so_8_sang_co_so_10(chuoi_hop_le)
elif co_so == 16:
    package_6.chuyen_co_so_16_sang_co_so_10(chuoi_hop_le)
else:
    print(co_so)