char_set = set()
while True:
    char = input("Nhập một ký tự (nhấn ESC để kết thúc): ")
    if char == '\x1b':
        break
    char_set.add(char)
tap_hop_sau_khi_xoa_so = {char for char in char_set if not char.isdigit()}
print("Tập hợp trước khi xóa các ký tự số:", char_set)
print("Tập hợp sau khi xóa các ký tự số:", tap_hop_sau_khi_xoa_so)
