## tìm số nhỏ nhất  và lớn nhất 

def xn(a,b,c):
    if a!=b!=c:
      x = max(a,b,c)
      n = min(a,b,c)
      print('số lớn nhất của ba số là :',x,n)
    else:
     print(a,b,c,'không đc bằng nhau')
    return 
a = int(input('nhập số nguyên a ở đây: '))
b= int(input('nhập số nguyên b ở đây: '))
c=int(input('nhập số nguyên c ở đây: '))
xn(a,b,c)