a = input("Nhập chuỗi ký tự a: ")
b = input("Nhập chuỗi ký tự b: ")
for i in range(1, len(a)):
    for j in range(1, len(b)):
        c = int(a[:i])
        d = int(b[i:])
        e = int(b[:j])
        f = int(b[j:])
        if c + d == e + f:
            print(f"{c}+{d}={e}+{f}")
            break
    else:
        continue
    break
else:
    print("Không tồn tại cách thêm dấu +")