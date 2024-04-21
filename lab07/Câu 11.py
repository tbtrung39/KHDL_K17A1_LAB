'''
Thi Olimpic: Giả sử một trường có n sinh viên tham gia thi Olimpic Tin học với các ngôn ngữ lập trình C++,
 Java và Python. Các sinh viên được đánh số từ 1 đến n.
- Ngôn ngữ C++ có a sinh viên dự thi, gồm các sinh viên có số thứ tự: ti,t2,., tr.
- Ngôn ngữ Java có b sinh viên dự thi, gồm các sinh viên có số thứ tự : ki,k2,..., kn.
- Ngôn ngữ Python có c sinh viên dự thi gồm các sinh viên có số thứ tự: h1,h2,..., hn.
Viết chương trình đưa ra danh sách các sinh viên chỉ thi một ngôn ngữ lập trình;
các sinh viên thi code trên 2 ngôn ngữ lập trình và các sinh viên dự thi cả 3 ngôn ngữ.
'''
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
