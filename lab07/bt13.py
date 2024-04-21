chuoi = input("Nhập vào chuỗi ký tự: ")

tu_dien = {}
for i in range(len(chuoi)):
    for j in range(i + 1, len(chuoi) + 1):
        chuoi_con = chuoi[i:j]
        if chuoi_con in tu_dien:
            tu_dien[chuoi_con] += 1
        else:
            tu_dien[chuoi_con] = 1

print("Từ điển:", tu_dien)
