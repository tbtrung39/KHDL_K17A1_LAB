import keyboard
chuoi_set = set()
print("Nhập các phần tử của tập hợp, ấn Esc để kết thúc:")
while True:
    phim = keyboard.read_event(suppress=True).name
    if phim == "esc":
        break
    chuoi_set.add(phim)
#chuoi_set = {phantu for phantu in chuoi_set if not phantu.isdigit()}
print("Tập hợp sau khi loại bỏ các phần tử số:", chuoi_set)
