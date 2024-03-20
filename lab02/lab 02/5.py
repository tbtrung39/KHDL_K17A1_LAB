#Viết chương trình cho phép nhập vào tháng (1->12) trong năm. Sau đó cho biết tháng đó có tên là gì và xuất kết quả ra màn hình. (1: January, 2: February, …).
month=int(input("moi nhap so thang:"))
if month==1:
    print("january")
elif month==2:
    print("february")
elif month==3:
    print("march")
elif month==4:
    print("april")
elif month==5:
    print("may")
elif month==6:
    print("june")
elif month==7:
    print("july")
elif month==8:
    print("august")
elif month==9:
    print("september")
elif month==10:
    print("october")
elif month==11:
    print("november")
elif month==12:
    print("december")
else:
    print("khong thoa man cac thang")