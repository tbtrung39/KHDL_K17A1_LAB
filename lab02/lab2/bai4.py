num =  int(input('Nhập số nguyên có ba chữ số : '))

if num<100:
    print('0')
else:
    num2 = (num//100) % 10
    print('hàng trăm của số ',num,'là :',num2)
