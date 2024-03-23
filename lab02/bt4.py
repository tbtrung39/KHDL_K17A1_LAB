gia_tri=int(input('Nhập giá trị:'))
if gia_tri<100:
    print('0')
else:
    gia_tri1=(gia_tri//100)%10
    print('Chữ số hàng trăm của giá trị là:',gia_tri1)