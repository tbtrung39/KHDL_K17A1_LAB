tham_nien_cong_tac=int(input("nhập thâm niên công tác(tháng) : "))
if tham_nien_cong_tac>0 and tham_nien_cong_tac <12:
    luong=2.34*1350000
    print(f"lương nhận {luong} đồng")
elif tham_nien_cong_tac >=12 and tham_nien_cong_tac<36:
    luong1=3.33*1350000
    print(f"lương nhận {luong1} đồng")
elif tham_nien_cong_tac>=36 and tham_nien_cong_tac < 60 :
    luong2=3.66*1350000
    print(f"lương nhận {luong2} đồng")
elif tham_nien_cong_tac>60:
    luong3=3.99*1350000
    print(f"lương nhận {luong3} đồng")
else: 
    print("số không hợp lệ ")