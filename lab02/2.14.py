import math
I1 = float(input("Nhập độ cường độ âm gốc từ nguồn (dB): "))
r = float(input("Nhập khoảng cách từ nguồn đến người nghe (m): "))
I = I1 - 20 * (math.log10(r))
if I >= 100:
    print("Người nghe nghe thấy âm.")
else:
    print("Người nghe không nghe thấy âm.")