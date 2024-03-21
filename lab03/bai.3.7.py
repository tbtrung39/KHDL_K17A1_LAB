n=int(input("nhập số nguyên dương n: "))
tong=1
if n <=0:
    print("số không hợp lệ!!!")
else:
    for i in range (1,n):
        tong+=1/(i+1)
    print("S =", tong)