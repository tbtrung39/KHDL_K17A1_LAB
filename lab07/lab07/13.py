W = input("Nhập vào chuỗi ký tự: ")
chuoi_dict = {}
for i in range(len(W)):
    for j in range(i + 1, len(W) + 1):
        chuoi = W[i:j]
        if chuoi in chuoi_dict:
            chuoi_dict[chuoi] += 1
        else:
            chuoi_dict[chuoi] = 1
print("Từ điển các chuỗi con và số lần xuất hiện:")
print(chuoi_dict)
