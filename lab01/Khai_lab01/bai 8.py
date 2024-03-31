Xa=float(input('Xa:'))
Ya=float(input('Ya:'))
Xb=float(input('Xb:'))
Yb=float(input('Yb:'))
Xc=float(input('Xc:'))
Yc=float(input('Yc:'))
a=lambda x,y,z:(x+y+z)/3
print(f'tọa độ trọng tâm của tam giác:({a(Xa,Xb,Xc):.2},{a(Ya,Yb,Yc):.2})')