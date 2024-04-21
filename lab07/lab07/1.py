tap_hop = set()
print("Nhập các kí tự vào tập hợp (Nhấn ESC để kết thúc):")
while True:
    ky_tu = input("Nhập kí tự: ")
    if ky_tu.lower() == 'esc':
        break
    tap_hop.add(ky_tu)
print("Tập hợp ban đầu:", tap_hop)
tap_hop_khong_so = {kt for kt in tap_hop if not kt.isdigit()}
print("Tập hợp sau khi loại bỏ các kí tự số:", tap_hop_khong_so)