#tính biểu thức có log
import math as m
x=float(input('nhập số x:'))
#math.log(a,b):log b của a
f=m.log(x,4) + m.log(2,x)
print('giá trị của biểu thức:',f)