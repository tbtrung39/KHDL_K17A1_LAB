chuoi = input("Nhập vào chuỗi ký tự: ")
dict_chuoi_con = {}
do_dai = len(chuoi)
for i in range(do_dai):
    for j in range(i + 1, do_dai + 1):
        chuoi_con = chuoi[i:j]
        dict_chuoi_con[chuoi_con] = None
print("Các chuỗi con trong từ điển:")
for key in dict_chuoi_con:
    print(key)