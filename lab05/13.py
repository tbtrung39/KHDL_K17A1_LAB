chuoi_a = input("Nhập chuỗi A: ")
chuoi_b = input("Nhập chuỗi B: ")
tim_thay = False
for i in range(1, len(chuoi_a)):
    for j in range(1, len(chuoi_b)):
        c, d = chuoi_a[:i] + '+' + chuoi_a[i:], chuoi_b[:j] + '+' + chuoi_b[j:]
        e = eval(c)
        f = eval(d)
        if e == f:
            print(f"{c} = {d} = {e} = {f}")
            tim_thay = True
            break
    if tim_thay:
        break
if not tim_thay:
    print("Không tồn tại cách đặt!")