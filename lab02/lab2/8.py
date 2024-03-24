luong_cb=1350000
TNCT=int(input("nhập thâm niên công tác:"))
if TNCT<12:
    luong=2.34*1350000
    print("lương của nhân viên là",luong)
if 12<=TNCT<36:
    luong2=3.33*1350000
    print("lương của nhân viên là:",luong2)
if 36<=TNCT<60:
    luong3=3.66*1350000
    print("lương của nhân viên là",luong3)
if TNCT>60:
    luong4=3.99*1350000
    print("lương của nhân viên là:",luong4)







