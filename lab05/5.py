'''Cho trước (hoặc nhập từ bàn phím) chuỗi ký tự Str. Hãy xóa đi tất cả các ký tự Str không 
phải là số, chuỗi ký tự còn lại sẽ là số. In ra kết quả chuỗi số này và thông báo cho biết 
chuỗi số đó có phải là số hoàn hảo không.'''
str= input( " nhap mot chuoi:")
for i in str :
    if '0'<= i <='9':
        chuoi_so_con_lai = ''.join(char for char in str if char.isdigit())
        print(" so con lai la",chuoi_so_con_lai)
tong = 0
so=int(chuoi_so_con_lai)
for j in range(1,so):
    if so % j == 0:
        tong += j
if tong==so:
    print(so," la so hoan hao")
else :
    print(so," khong phai la so hoan hao")