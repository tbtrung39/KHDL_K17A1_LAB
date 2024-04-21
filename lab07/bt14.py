dict = {}
for i in range(1, 101):
    so_nhi_phan = ""
    thuong = i
    while thuong > 0:
        so_nhi_phan = str(thuong % 2) + so_nhi_phan
        thuong = thuong // 2
    dict[i] = so_nhi_phan
print("Từ điển chứa các số từ 1 đến 100 và chuỗi nhị phân tương ứng: ",dict)