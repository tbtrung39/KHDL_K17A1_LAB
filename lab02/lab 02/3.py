# Viết chương trình cho phép nhập vào thứ (1->7) trong tuần. Sau đó cho biết thứ đã nhập có tên là gì và xuất kết quả ra màn hình. (1: Sunday, 2: Monday, …)
day_number = int(input("Nhập số thứ trong tuần (1->7): "))
if day_number == 1:
    print("Sunday")
elif day_number==2:
    print("Monday")
elif day_number==3:
    print("Tuesday")
elif day_number==4:
    print("wedesday")
elif day_number==5:
    print("thurday")
elif day_number==6:
    print("friday")
elif day_number==7:
    print("saturday")
else:
    print("khong thoa man cac thu trong tuan")