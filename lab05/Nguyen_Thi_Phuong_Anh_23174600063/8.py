chuoi = input("Nhập chuỗi ký tự: ")
do_dai = len(chuoi)
chuoi_max = ""
for i in range(do_dai):
    for j in range(i + 1, do_dai + 1):
        phan_tu = chuoi[i:j]
        if phan_tu == phan_tu[::-1]:
            if len(phan_tu) > len(chuoi_max):
                chuoi_max = phan_tu
if chuoi_max:
    print(f"Chuỗi con dài nhất và lặp lại nhau trong chuỗi là: {chuoi_max}")
else:
    print("Không có")