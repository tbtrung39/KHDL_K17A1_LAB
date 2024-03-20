#Viết chương trình tính lương của nhân viên dựa theo thâm niên công tác (TNCT) 
tnct=int(input("moi nhap tham nien cong tac:"))
luong_co_ban=1350000
if tnct<12:
    he_so=2.34
elif (tnct >= 12) or (tnct<36):
    he_so=3.33
elif (tnct>=36) or (tnct<60):
    he_so=3.66
else:
    he_so=3.99
    print(f"Lương của nhân viên là: {he_so*luong_co_ban} đồng")
