# Số lượng sinh viên và các thứ tự tương ứng
n = 10
a = 3
b = 4
c = 5

# Tạo set để lưu danh sách sinh viên tham gia từng ngôn ngữ
C = set()
Java = set()
Python = set()

# Thêm sinh viên vào danh sách tương ứng
for i in range(1, a + 1):
    C.add("ti" + str(i))
    C.add("tz" + str(i))
    C.add("." + str(i))
    C.add("tn" + str(i))

for i in range(1, b + 1):
    Java.add("ki" + str(i))
    Java.add("k2" + str(i))
    Java.add("..." + str(i))
    Java.add("kn" + str(i))

for i in range(1, c + 1):
    Python.add("hi" + str(i))
    Python.add("he" + str(i))
    Python.add("..." + str(i))
    Python.add("hn" + str(i))

# In danh sách sinh viên từng ngôn ngữ
print("Danh sách sinh viên thi ngôn ngữ C++:")
print(C)

print("\nDanh sách sinh viên thi ngôn ngữ Java:")
print(Java)

print("\nDanh sách sinh viên thi ngôn ngữ Python:")
print(Python)
