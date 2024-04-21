ki_tu = set()
print("Nhập các kí tự (ESC để kết thúc): ")
while True:
    set_a = input()
    if set_a == "":
        break
    ki_tu.add(set_a) if not set_a.isdigit() else None
print("Set sau khi loại bỏ số: ", ki_tu)