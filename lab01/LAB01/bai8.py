import math
x =  float(input('nhập x tính log  ở đây : '))
fx= math.log(x,4)+ math.log(2,x)
fx = round(fx,2)
print('giá trị của biểu thức log trên là  : ',fx)