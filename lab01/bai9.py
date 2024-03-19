n = int(input("nhập só tung xúc sắc: "))
xac_suat_khong_ra_sau_trong_mot_lan=5/6

xac_suat_khong_ra_sau_trong_n_lan=xac_suat_khong_ra_sau_trong_mot_lan**n

xac_suat_ca_ba_xuc_sac_ko_ra_sau=1-xac_suat_khong_ra_sau_trong_n_lan

print(f"xác suất là: {xac_suat_ca_ba_xuc_sac_ko_ra_sau:.2f}")