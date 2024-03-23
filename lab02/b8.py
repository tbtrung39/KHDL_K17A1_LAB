TNCT = int(input("Nhập số thâm niên công tác là:"))
luonng_can_ban = 1350000
if TNCT >= 60:
    luong1 = 3.99 * luonng_can_ban
    print("Lương của nhân viên là:",luong1)
if TNCT >= 36 and TNCT < 60:
    luong2 = 3.66 * luonng_can_ban
    print("Lương của nhân viên là:",luong2)
if TNCT >= 12 and TNCT < 36:
    luong3 = 3.33 * luonng_can_ban
    print("Lương của nhân viên là:",luong3)
if TNCT < 12:
    luong4 = 2.34 * luonng_can_ban
    print("Lương của nhân viên là:",luong4)