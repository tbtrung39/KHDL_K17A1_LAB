import math
I = float(input("Nhập mức cường độ âm I (dB): "))
D = float(input("Nhập khoảng cách D (m): "))

if I - 20 * math.log10(D) > 100:
    print("Người này không nghe thấy âm.")
else:
    print("Người này nghe thấy âm")