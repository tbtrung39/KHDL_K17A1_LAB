month = int(input('nhập số tháng bạn cần biết ngày ở đây :'))
year =  int(input('nhập năm của tháng bạn muốn kiểm tra : '))

if 0<month<=12 and year >0:
    if month<8 and month%2!=0:
        print('tháng ',month,'là tháng có 31 ngày ')
    elif 8<=month and month%2 == 0:
        print('tháng ',month,'là tháng có 31 ngày ')
    elif 2<month<8 and month%2 ==0:
        print('tháng ',month,'là tháng có 30 ngày ')
    elif 8< month and month %2!=0:
        print('tháng ',month,'là tháng có 30 ngày ')
    elif month ==2:
        if year %4==0 or year %400==0:
            print('do năm bạn nhâp là năm nhuận  nên tháng 2 có 29 ngày')
        else:
            print('do năm bạn nhập là năm k nhuận nên tháng 2 có 28 ngày')
else:
    print('không có tháng đó ')

