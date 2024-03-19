import math
I = float(input("Nhập mức cường độ âm I (dB): "))
D = float(input("Nhập khoảng cách D (m): "))
muc_cuong_do_am_I = I - 20 * (math.log10(D / 1))  

if muc_cuong_do_am_I >= 100:
    print("Người này nghe được.")
else:
    print("Người này không nghe được.")