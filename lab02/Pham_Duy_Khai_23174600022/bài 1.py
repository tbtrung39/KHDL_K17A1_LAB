a=int(input('nhập tháng:'))  
if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
    print(f'tháng {a} có 31 ngày')
if a==4 or a==6 or a==9 or a==11:
    print(f'tháng {a} có 30 ngày') 
if a==2:
    print(f'tháng {a} có 29 ngày')
    