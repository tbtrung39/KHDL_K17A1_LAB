xA,yA=map(float,input("Nhap toa do dinh A :").split())
xB,yB=map(float,input("Nhap toa do dinh B :").split())
xC,yC=map(float,input("Nhap toa do dinh C :").split())
x_trong_tam=(xA+xB+xC)/3
y_trong_tam=(yA+yB+yC)/3
print(f"Trong tam cua tam giac do la :({x_trong_tam:.2f};{y_trong_tam:.2f})")