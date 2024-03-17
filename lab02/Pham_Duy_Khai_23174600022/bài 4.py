a=int(input('nhập số:'))
if a/100>=10:
    print(f'chữ số hàng trăm:{int((a%1000-a%100)/100)}')
elif a/100>=1:
    print(f'chứ số hàng trăm:{a//100}')
else:
    print(f'chữ số hàng trăm:{0}')
    