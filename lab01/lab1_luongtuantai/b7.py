print("nhập tọa độ A(x,y)")
x_A=float(input("nhập tọa độ x_A: "))    
y_A=float(input("nhập tọa đọ y_A: "))
print("nhập tọa độ B(x,y)")
x_B=float(input("nhập tọa độ x_B: "))
y_B=float(input("nhập tọa độ Y_B: "))
print("nhập tọa độ C(x,y)")
x_C=float(input("nhập tọa độ x_C: "))
y_C=float(input("nhập tọa độ y_C: "))
x_trong_tam= (x_A+x_B+x_C)/3
y_trong_tam= (y_A+y_B+y_C)/3
x_trong_tam=round(x_trong_tam,2)
y_trong_tam=round(y_trong_tam,2)
print("tọa độ trọng tâm của tam giác là ({},{})".format(x_trong_tam,y_trong_tam))