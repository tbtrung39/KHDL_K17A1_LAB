while True:
    n = input("Nhập từ bàn phím chuỗi ký tự n (nhập 'esc' để kết thúc): ")
    if n == "esc":
        break
    else:
        m = set(n)
        m.difference_update(set("0123456789"))
        print(f"Tập hợp sau khi loại bỏ các ký tự số: {m}")
