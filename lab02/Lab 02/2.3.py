'''
Viết chương trình cho phép nhập vào thứ (1->7) trong tuần. 
Sau đó cho biết thứ đã nhập có tên là gì và xuất kết quả ra màn hình. 
(1: Sunday, 2: Monday, …)
'''
#Nhap thu trong tuan 
thu_trong_tuan = int(input("Nhap thu trong tuan: "))
if thu_trong_tuan == 1 :
    print("Monday")
elif thu_trong_tuan == 2 :
    print("Tuesday")
elif thu_trong_tuan == 3 :
    print("Wednesday")
elif thu_trong_tuan == 4 :
    print("Thurday")
elif thu_trong_tuan == 5 :
    print("Friday")
elif thu_trong_tuan == 6 :
    print("Saturday")
elif thu_trong_tuan == 7 :
    print("Sunday")