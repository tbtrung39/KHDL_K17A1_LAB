TNCT=float(input("Nhập tnct:"))
lg_cban=1350000
if TNCT>=60:
    hso=3.99
elif TNCT>=36:
    hso=3.66
elif TNCT>=12:
    hso=3.33
elif TNCT<12:
    hso=2.34
salary=hso*lg_cban
print("Lương nvien=",salary)