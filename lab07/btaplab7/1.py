tao_set=set()
while True:
    char=input('Nhập các phần tử là kí tự (Nhấn ESC để kết thúc) :')
    if char=='ESC':
        break
    if not char.isdigit():
        tao_set.add(char)
print('Chuỗi sau khi loại bỏ số là :',tao_set)
