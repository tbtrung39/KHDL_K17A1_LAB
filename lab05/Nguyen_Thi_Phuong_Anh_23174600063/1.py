str = input('Nhập vào một số kí tự:')
print("Chuỗi kí tự vừa nhập là:",str)
dem = 0
for i in str :
    if "0" <= i <= "9":
        dem += 1
print("Số các kí tự là số trong chuỗi đã nhập = ", dem )