import math

I_0 = float(input("Nhập mức cường độ âm thanh tại nguồn phát I_0 (dB): ")) 
D = float(input("Nhập khoảng cách từ nguồn phát đến người nghe D (m): "))
D_0 = 1  # Giả sử khoảng cách mức độ tham chiếu là 1m

I = I_0 - 20 * math.log10(D_0 / D)

if I >= 100:
    print("Người nghe có thể nghe thấy âm.")
else:
    print("Người nghe không nghe thấy âm.")