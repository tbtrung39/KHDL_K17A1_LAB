import sys
sys.path.append("lab10\doi_co_so")

import doi_co_so

n=doi_co_so.nhap_so()
print(f'chuyen {n} sang he nhi phan:')
print(doi_co_so.chuyen_sang_he_nhi_phan(n))
print(f'chuyen {n} sang he co so 8:')
print(doi_co_so.chuyen_sang_he_bat_phan(n))
print(f'chuyen {n} sang he co so 16:')
print(doi_co_so.chuyen_sang_he_16(n))

chuoi_hop_le = doi_co_so.nhap_va_loc_chuoi()
co_so = doi_co_so.xac_dinh_co_so(chuoi_hop_le)

if co_so == 2:
    doi_co_so.chuyen_co_so_2_sang_co_so_10(chuoi_hop_le)
elif co_so == 8:
    doi_co_so.chuyen_co_so_8_sang_co_so_10(chuoi_hop_le)
elif co_so == 16:
    doi_co_so.chuyen_co_so_16_sang_co_so_10(chuoi_hop_le)
else:
    print(co_so)