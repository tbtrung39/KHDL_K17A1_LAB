months=int(input("nhap vao mot thang (1->12): "))
if months >12 or months <1:
    print("vui long nhap lai")
else:
    if months ==1:
        print(1,":january")
    elif months ==2:
        print(2,":Feburary")
    elif months ==3:
        print(3,":March")
    elif months ==4:
        print(4,":Apirl")
    elif months ==5:
        print(5,":May")
    elif months ==6:
        print(6,":June")
    elif months ==7:
        print(7,":July")
    elif months ==8:
        print(8,":August")
    elif months ==9:
        print(9,":September")
    elif months ==10:
        print(10,":October")
    elif months ==11:
        print(11,":November")
    elif months ==12:
        print(12,":December")