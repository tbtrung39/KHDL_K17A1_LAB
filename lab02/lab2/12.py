import math
a=float(input(' nhập giá trị a:'))
b=float(input(' nhập giá trị b:'))
c=float(input(' nhập giá trị c:'))
d=float(input(' nhập giá trị d:'))
r=float(input(' nhập giá trị r:'))
e=pow(a-c,2)+pow(b-d,2)
khoang_cach=math.sqrt(e)
if khoang_cach>r:
    print("M nằm ngoài đường tròn")
elif khoang_cach<r:
    print('M nằm trong đường tròn')    
else:
    print('M nằm trên đường tròn')