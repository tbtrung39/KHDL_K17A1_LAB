import doicoso2 as f
chuoi = input("nhap vao mot chuoi ki tu: ")
chuoi_hop_le = f.loc_ki_tu(chuoi)
co_so = f.xac_dinh_co_so(chuoi_hop_le)
if co_so ==2:
    print(f"chuoi {chuoi_hop_le} trong he co so 2 truong duong voi {f.chuyen_doi_nhi_phan_sang_thap_phan(chuoi_hop_le)} trong he 10")
if co_so ==8:
    print(f"chuoi {chuoi_hop_le} trong he co so 8 truong duong voi {f.chuyen_doi_bat_phan_sang_thap_phan(chuoi_hop_le)} trong he 10")
if co_so == 16:
    print(f"chuoi {chuoi_hop_le} trong he co so 16 truong duong voi {f.chuyen_doi_thap_luc_phan_sang_thap_phan(chuoi_hop_le)} trong he 10")
    
