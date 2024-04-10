list=[]
list1=[]
list2=[]
while True:
    print("1.gửi tiền ")
    print("2. rút tiền ")
    print("3.Lưu và in ra số tiền thực trong tài khoản ")
    n=int(input("Nhập lựa chọn của bạn "))
    if n ==1 :
        D=int(input("nhập số tiền gửi :"))
        list1.append(D)
    elif n ==2 :
        W=int(input("Nhập số tiền rút :"))
        list2.append(W)
        if sum(list1)-sum(list2) < 0 :
            print("số tiền trong tài khoản của bạn không đủ mời nhập lại ")
            list2.remove(W)
    else:
        print(" số tiền thực trong tài khoản của bạn là :",sum(list1)-sum(list2) )
        
    