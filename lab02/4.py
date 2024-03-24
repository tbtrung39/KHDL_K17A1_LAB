num =  int(input('nhập số nguyển cần xuất hàng trăm ra ở đây : '))
if num<100:
    print('0')
else:
    num2 = (num//100) % 10
    print('hàng trăm của số ',num,'là :',num2)
