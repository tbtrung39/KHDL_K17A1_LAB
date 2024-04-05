str = input("Nhập văn bản hoàn đầy đủ: ")
don = input("Nhập vào 1 từ đơn: ")
s = 0
tu_don = str.split()
for i in tu_don:
    if i == don:
        s += 1
print(f"Từ {don} xuất hiện {s} lần")