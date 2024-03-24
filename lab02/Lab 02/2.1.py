'''
Viết chương trình nhập vào một tháng và cho biết tháng đó có bao nhiêu ngày.
'''
#nhập vào 1 tháng có bao nhiêu ngày
a=int(input("nhập tháng cần tìm:"))
if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
    print(a,"là tháng có 31 ngày")
if a==4 or a==6 or a==9 or a==11:
    print(a,"là tháng có 30 ngày")
if a==2:
    print('tháng này có 29 ngày')