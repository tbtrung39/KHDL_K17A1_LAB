from pk2 import modul2

a = int(input("NHập giá trị d: ")) #a là độ dài 1 cạnh của hình vuông

chu_vi = modul2.ChuviHinhvuong(a)
print(f"Chu vi hình vuông cạnh {a} là: {chu_vi}")

dien_tich = modul2.DientichHinhvuong(a)
print(f"Diện tích hình vuông cạnh {a} là: {dien_tich}")