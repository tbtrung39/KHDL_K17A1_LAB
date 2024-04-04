str = input("Nhập văn bản hoàn chỉnh: ")
a = input("Nhập vào 1 từ đơn: ")
s = 0
tu_don = str.split()
for i in tu_don:
    if i == a:
        s += 1
print(f"Từ {a} xuất hiện {s} lần")