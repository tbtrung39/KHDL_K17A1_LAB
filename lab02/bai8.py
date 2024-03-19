TNCT=int(input("nhập số thâm niên công tác: "))
luong_can_ban=1350000
if TNCT>0 and TNCT <12:
    he_so1=2.34
    luong=he_so1*luong_can_ban
    print("số tiền lương:", luong)
elif TNCT>=12 and TNCT <36:
    he_so2=3.33
    luong=he_so2*luong_can_ban
    print("số tiền lương:", luong)
elif TNCT>=36 and TNCT <60:
    he_so3=3.66
    luong=he_so3*luong_can_ban
    print("số tiền lương:", luong)
elif TNCT>=60:
    he_so4=3.99
    luong=he_so4*luong_can_ban
    print("số tiền lương:", luong)
else:
    print("số thâm niên không phù hợp!!!")