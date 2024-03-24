n=int(1)
print("---menu---")
print("1.cafe")
print("2.Cam vắt ")
print("3.nước ép cốt dừa")
print("4.Nước lọc")
print("5.Nước dừa ")
print("6.kết thúc trọn")

while True:
    n=int(input("nhập nước uống(1-6) : "))
    if n==1 :
        print("đã thêm 1 cafe")
    elif n==2:
        print("đã thêm 1 cam vắt")
    elif n==3:
        print("đã thêm 1 nước ép cốt dừa ")
    elif n==4:
        print("đã thêm 1 nước lọc ")
    elif n==5:
        print("đã thêm 1 nước dừa")
    elif n<=0 or n>=6:
        print("kết thúc trọn đồ")
        break