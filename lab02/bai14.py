nguong_nghe = 100
I0 = float(input("Nhập mức cường độ âm tại nguồn phát (dB): "))
r0 = float(input("Nhập khoảng cách từ nguồn phát âm đến người nghe (m): "))
r = float(input("Nhập khoảng cách từ nguồn phát âm đến nguồn âm cầu (m): "))

# Tính mức cường độ âm tại vị trí người nghe
I = I0 * (r0 / r)**2

# Kiểm tra xem người nghe có nghe thấy âm không
if I >= nguong_nghe:
    print("Người nghe có nghe thấy âm.")
else:
    print("Người nghe không nghe thấy âm.")
