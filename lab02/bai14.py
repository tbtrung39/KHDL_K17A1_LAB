import math

I = float(input("Nhập mức cường độ âm I (dB): "))
D = float(input("Nhập khoảng cách D (m): "))

D0 = 1  # Khoảng cách tham chiếu

A = 20 * math.log10(D / D0)
I_nguoi_nghe = I - A

if I_nguoi_nghe > 100:
    print("Người này sẽ nghe thấy âm.")
else:
    print("Người này không nghe thấy âm.")