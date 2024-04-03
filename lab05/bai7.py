van_ban = input("Nhập văn bản khuôn: ")
tim = input("Nhập từ cần tìm: ")
gt = 0
tu_don = van_ban.split()
for tu in tu_don:
    if  tu == tim:
        gt = gt + 1
print(f"Từ '{tim}' xuất hiện {gt} lần")
