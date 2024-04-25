def find_ucln(ts,ms):
    while ms != 0:
        ts , ms = ms , ts%ms
    return ts
ts = int(input("nhập vào tử số: "))
ms = int(input("nhập vào mẫu số: "))
print(f"giá trị sau khi chia tử số {ts} và mẫu số {ms} cho ucln {find_ucln(ts,ms)} là {(ts/find_ucln(ts,ms))/(ms/find_ucln(ts,ms))}")
