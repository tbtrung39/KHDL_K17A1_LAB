ky_tu = set()
print("Nhập các kí tự vs esc để kêt thức: ")
while True:
    ki_tu = input()
    if ki_tu == "":
        break
    ky_tu.add(ky_tu) if not ki_tu.isdigit() else None
print("set sáu khi loại bỏ số là: ",)