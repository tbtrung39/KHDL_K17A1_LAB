num1  = int(input('nhập số thứ 1 ở đây'))
num2  =  int(input('nhập số thứ 2 ở đây '))

a  =  num1* num2
for i  in range(1,a+1,1):
    if i % num1 ==0 and i % num2 ==0:
        print('bội chung nhỏ nhất của 2 sô vừa nhập là : ',i)
        break
