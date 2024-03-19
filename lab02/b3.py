day = int(input("nhap vao thu (1-7) trong tuan: "))
if day <1 or day > 7:
    print("vui long nhap lai")
else:
    if day ==2:
        print(2,": Monday")
    elif day ==3:
        print(3,": Tuesday")
    elif day ==4:
        print(4,": Wednessday")
    elif day == 5:
        print(5,": Thursday")
    elif day == 6:
        print(6,": Friday")    
    elif day ==1:
        print(1,": Sunday")