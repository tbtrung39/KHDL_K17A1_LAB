#Viết chương trình nhập vào tháng và xem tháng đó có bao nhiêu ngày
n = int(input("Nhập vào tháng:"))
if n==1:
    result=31
elif n==3:
    result=31
elif n==4:
    result=30
elif n==5:
    result=31
elif n==6:
    result=30
elif n==7:
    result=31
elif n==8:
    result=31
elif n==9:
    result=30
elif n==10:
    result=31
elif n==11:
    result=30
elif n==12:
    result=31
elif n==2:
    print("Kiểm tra có phải năm nhuận không!")
    nam=int(input("Nhập năm:"))
    if (nam%4==0 and nam%100!=0) or (nam%400==0):
        print("Tháng 2 có 29 ngày")
    else:
        print("Tháng 2 có 28 ngày")
else:
    print("Lỗi!! nhập lại đi")
print(f"Tháng {n} có {result} ngày")