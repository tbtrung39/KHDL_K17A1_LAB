n = int(input("Nhập số lượng tuple:"))
tuples = []
for i in range(n):
    ten = input("Nhập tên:")
    tuoi = int(input("Nhập tuổi:"))
    diem = int(input("Nhập điểm:"))
    tuples.append((ten,tuoi,diem))

tuples.sort( key = lambda x: (x[0], x[1], x[2]))
print("Các tuple sau khi được sắp xếp :")
for t in tuples:
    print(t)