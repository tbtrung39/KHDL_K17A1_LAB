str1 = input("Nhap chuoi str1 la:")
str2 = input("Nhap chuoi str2 la:")
do_dai1 = len(str1)
do_dai2 = len(str2)
tron1 = 0
tron2 = 0
hop = ''
while tron1 < do_dai1 or tron2 < do_dai2:
    if tron1 < do_dai1:
        hop += str1[tron1]
        tron1 += 1
    if tron2 < do_dai2:
        hop += str2[tron2]
        tron2 += 1
print("Sau khi tron sau str1 va str2 la:",hop)