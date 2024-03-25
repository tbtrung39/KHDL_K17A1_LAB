import math
a=int(input("Nhập gtri a:"))
b=int(input("Nhập gtri b:"))
x=c=int(input("Nhập gtri c:"))
y=d=int(input("Nhập gtri d:"))
r=int(input("Nhập gtri r:"))

kcach= math.sqrt((x-a)**2 +(y-b)**2)
if kcach>r:
    print("Điểm M nằm ngoài đg tròn")
elif kcach==r:
    print("Điểm M nằm trên đg tròn")
else:
    print("Điểm M nằm trong đg tròn")