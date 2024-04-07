#Nhập từ bàn phím một chuỗi ký tự Str. Hãy đếm sô các ký tự là số trong chuỗi ký tự Str 
#và in kết quả ra màn hình. 
a = input(" nhap mot chuoi:")
tong=0
for i in a :
    if '0'<=i<='9' :
        tong+=1
print(tong)