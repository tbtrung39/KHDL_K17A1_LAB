chuoi = input("Nhập chuỗi: ")

max_length = 0  
var_dang_xet = ''  
list_con = 1  
for i in range(1, len(chuoi)):
    if chuoi[i] == chuoi[i - 1]:
        list_con += 1
    else:
        if list_con > max_length:
            max_length = list_con
            var_dang_xet = chuoi[i - 1]
        list_con = 1



if max_length == 1:
    print("Không tồn tại chuỗi con nào có độ dài lớn hơn 1 và bao gồm các ký tự giống nhau.")
else:
    print("Chuỗi con có độ dài cực đại và bao gồm các ký tự giống nhau là:", var_dang_xet * max_length)