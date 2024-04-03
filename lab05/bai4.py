str1 = input("Nhập chuối 1: ")
str2 = input("Nhập chuỗi 2: ")
dai1 = len(str1)
dai2 = len(str2)
hop = ""
gt1 = 0
gt2 = 0
while gt1 < dai1 or gt2 < dai2:
    if gt1 < dai1:
        hop+= str1[gt1]
        gt1+=1
    if gt2 < dai2:
        hop+= str2[gt2]
        gt2+=1
print("chuỗi sau khi trộn vs nhau là: ", hop)