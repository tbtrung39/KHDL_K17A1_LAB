# tính chu vi và diện tích hình tròn
def SC(r):
    if r>0:
     c= 2*3.14*r
     s = 3.14*r**2
     print('chu vi và bán kính là: ',c,s)
    else:
       print('bán kính phải lớn hơn không')
r = int(input('nhập bán kính ở đây: '))
SC(r)