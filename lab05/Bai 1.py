'''
Nhập từ bàn phím một chuỗi ký tự Str. 
Hãy đếm số các ký tự là số trong chuỗi ký tự Str và in kết quả ra màn hình.
'''
chuoi = input("Nhập vào một chuỗi: ")
count1 = 0
#Sử dụng vòng lặp xét từng ký tự
for i in chuoi:
    if i.isnumeric():
        count1 += 1
print("Số lượng ký tự là số trong chuỗi trên là:", count1)
#Sử dụng vòng lặp xét từng chỉ mục
count2 = 0
for j in range(len(chuoi)):
    if chuoi[j].isnumeric():
        count2 +=1
print("Số lượng ký tự là số trong chuỗi là:", count2)
