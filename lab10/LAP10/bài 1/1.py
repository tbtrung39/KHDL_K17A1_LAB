from package_1 import my_Triange as p
a=float(input('nhập độ dài cạnh thứ nhất:'))
b=float(input('nhập độ dài cạnh thứ hai:'))
c=float(input('nhập độ dài cạnh thứ ba:'))
if p.Is_TamGiac(a,b,c):
    print(f'chu vi tam giác: {p.chuViTamGiac(a,b,c)} ')
    print(f'diện tích tam giác: {p.S_TamGiac(a,b,c)}')
    
