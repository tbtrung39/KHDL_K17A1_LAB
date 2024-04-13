tuple = []
ten = input("Nhap ten nguoi dung: ")
tuoi = int(input("Nhap tuoi: "))
diem = int(input("Nhap diem: "))
tuple.append((ten, tuoi, diem))
tuple.sort(key=lambda x:(x[0], x[1], x[2]))
print(tuple)