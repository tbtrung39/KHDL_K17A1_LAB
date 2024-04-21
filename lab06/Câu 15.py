'''
 Viết chương trình sắp xếp tuple (name, age, score) theo thứ tự tăng dần, 
 Name là string, age và height là number. Tuple được nhập vào bởi người dùng. 
 Tiêu chí sắp xếp là: Sắp xếp theo name sau đó sắp xếp theo age, sau đó sắp xếp theo score. 
 Ưu tiên là tên > tuổi > điểm.
 '''
n = int(input("Nhập số lượng tuple: "))
tuples = []

# Nhập thông tin cho từng tuple
for i in range(n):
    ten = input("Nhập tên: ")
    tuoi = int(input("Nhập tuổi: "))
    diem = int(input("Nhập điểm: "))
    tuples.append((ten, tuoi, diem))

# Sắp xếp danh sách các tuple theo tiêu chí (tên, tuổi, điểm)
tuples.sort(key=lambda x: (x[0], x[1], x[2]))

# In danh sách các tuple đã sắp xếp
print("Các tuple sau khi được sắp xếp:")
for t in tuples:
    print(t)

