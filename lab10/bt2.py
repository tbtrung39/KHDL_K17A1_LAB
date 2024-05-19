from pk2 import my_square

a = int(input("NHập giá trị d: ")) #a là độ dài 1 cạnh của hình vuông

chu_vi = my_square.ChuviHinhvuong(a)
print(f"Chu vi hình vuông cạnh {a} là: {chu_vi}")

dien_tich = my_square.DientichHinhvuong(a)
print(f"Diện tích hình vuông cạnh {a} là: {dien_tich}")