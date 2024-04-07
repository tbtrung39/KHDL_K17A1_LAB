a=input("nhập chuỗi: ")
b = 0  
c = ''  
d = 1  
for i in range(1,len(a)):
    if a[i]==a[i-1]:
        d+=1
    else:
        if d>b:
            b=d
            c=a[i-1]
        d=1
if b==1:
    print("không có.")
else:
    print(f'chuỗi con có độ dài max là:{b*c}')