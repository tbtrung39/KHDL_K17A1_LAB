import math
i= float(input("Nhập mức cường độ âm I (dB): "))
d = float(input("Nhập khoảng cách D (m): "))
d0 = 1  
do_giam = 20 * math.log10(d / d0)
if i - do_giam >= 100:
    print("Người nghe có thể nghe thấy âm từ nguồn âm cầu.")
else:
    print("Người nghe không nghe thấy âm từ nguồn âm cầu.")