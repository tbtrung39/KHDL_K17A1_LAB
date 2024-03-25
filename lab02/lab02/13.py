I0 = float(input("Nhập mức cường độ âm: "))
D = float(input("Nhập khoảng cách từ nguồn phát sóng đến người nghe: "))

# Tính mức cường độ âm thanh tại vị trí người nghe
I = I0 * (1 / D)**2

if I > 100:
    print("Người nghe nghe thấy âm.")
else:
    print("Người nghe không nghe thấy âm.")