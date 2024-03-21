x1 = float(input("Nhập vào giá trị x1 của đỉnh A:"))
y1 = float(input("Nhập vào giá trị y1 của đỉnh A:"))
x2 = float(input("Nhập vào giá trị x2 của đỉnh B:"))
y2 = float(input("Nhập vào giá trị y2 của đỉnh B:"))
x3 = float(input("Nhập vào giá trị x3 của đỉnh C:"))
y3 = float(input("Nhập vào giá trị y3 của đỉnh C:"))
def tinh_trong_tam(x1,x2,x3,y1,y2,y3):
    x_trong_tam = (x1+x2+x3)/3
    y_trong_tam = (y1+y2+y3)/3
    return round(x_trong_tam, 2), round(y_trong_tam, 2)
x_trong_tam, y_trong_tam = tinh_trong_tam(x1,x2,x3,y1,y2,y3)
print(f"Trọng tâm của tam giác có toa độ là ({x_trong_tam}), ({y_trong_tam}")