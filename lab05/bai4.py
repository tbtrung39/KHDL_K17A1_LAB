str1 = input("Nhập chuỗi ký tự thứ nhất: ")
str2 = input("Nhập chuỗi ký tự thứ hai: ")
chuoi_tron = ''
do_dai_str1 = len(str1)
do_dai_str2 = len(str2)
phan_tu_str1 = 0
phan_tu_str2 = 0
while phan_tu_str1 < do_dai_str1 or phan_tu_str2 < do_dai_str2:
    if phan_tu_str1 < do_dai_str1:
        chuoi_tron += str1[phan_tu_str1]
        phan_tu_str1 += 1
    if phan_tu_str2 < do_dai_str2:
        chuoi_tron += str2[phan_tu_str2]
        phan_tu_str2 += 1
print("Chuỗi sau khi trộn:", chuoi_tron)