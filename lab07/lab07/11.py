n = int(input("Nhập số lượng sinh viên: "))
C = set()
Java = set()
Python = set()
a = int(input("Nhập số lượng sinh viên dự thi ngôn ngữ C++: "))
b = int(input("Nhập số lượng sinh viên dự thi ngôn ngữ Java: "))
c = int(input("Nhập số lượng sinh viên dự thi ngôn ngữ Python: "))
for i in range(a):
    sv = int(input(f"Sinh viên dự thi ngôn ngữ C++ - Sinh viên thứ {i + 1}: "))
    C.add(sv)
for i in range(b):
    sv = int(input(f"Sinh viên dự thi ngôn ngữ Java - Sinh viên thứ {i + 1}: "))
    Java.add(sv)
for i in range(c):
    sv = int(input(f"Sinh viên dự thi ngôn ngữ Python - Sinh viên thứ {i + 1}: "))
    Python.add(sv)
only_C = C - Java - Python
only_Java = Java - C - Python
only_Python = Python - C - Java
both_C_Java = C & Java - Python
both_C_Python = C & Python - Java
both_Java_Python = Java & Python - C
all_three = C & Java & Python
# In ra danh sách các sinh viên
print("Sinh viên chỉ dự thi một ngôn ngữ:")
print("C++:", only_C)
print("Java:", only_Java)
print("Python:", only_Python)
print("\nSinh viên thi code trên 2 ngôn ngữ:")
print("C++ và Java:", both_C_Java)
print("C++ và Python:", both_C_Python)
print("Java và Python:", both_Java_Python)
print("\nSinh viên dự thi cả ba ngôn ngữ:")
print("C++, Java, và Python:", all_three)
