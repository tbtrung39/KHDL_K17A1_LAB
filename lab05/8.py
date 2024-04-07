'''Cho trước hoặc nhập từ bàn phím chuỗi ký tự Str. Hãy tìm một chuỗi ký tự con có độ 
dài cực đại và bao gồm các phần tử giống nhau của chuỗi ký tự trên. Ví dụ : Chuỗi ký tự 
nhập vào là:”aabbcc” thì chuỗi ký tự in ra sẽ là : “bbb”'''
chuoi = input(" nhap mot chuoi")
a = input(" nhap ki tu con")
b = chuoi.rfind(a)
print(b)