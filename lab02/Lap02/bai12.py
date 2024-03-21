a=float(input('Nhập giá trị a :'))
b=float(input('Nhập giá trị b :'))
c=float(input('Nhập giá trị c :'))
d=float(input('Nhập giá trị d :'))
r=float(input('Nhập bán kính r: '))
khoang_cach=((c-a)**2+(d-b)**2)**0.5
if khoang_cach>r:
    print('Điểm M nằm ngoài đường tròn')
elif khoang_cach==r:
    print('Điểm M nằm trên đường tròn')
else:
    print('Điểm M nằm trong đường tròn')