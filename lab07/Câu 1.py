'''
Viết chương trình khỏi tạo một set với các phần tử là ký tự được nhập từ bàn phím.
Việc nhập dữ liệu kết thúc khi bấm phím ESC. Xóa các phần tử là ký tự số khỏi tập hợp.
'''
set = set()
while True:
    char=input('Nhập các phần tử là kí tự (Nhấn ESC để kết thúc) :')
    if char=='ESC':
        break
    if not char.isdigit():
        set.add(char)
print('Chuỗi sau khi loại bỏ số là :',set)