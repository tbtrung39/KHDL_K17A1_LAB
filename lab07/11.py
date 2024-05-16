# Số lượng sinh viên dự thi theo từng ngôn ngữ
a = 3
b = 2
c = 4

# Danh sách sinh viên theo từng ngôn ngữ
t = [1, 2, 3]
k = [2, 3]
h = [3, 4, 5, 6]

# Số lượng sinh viên tham gia thi
n = 6

only_cpp = set(t) - set(k) - set(h)
only_java = set(k) - set(t) - set(h)
only_python = set(h) - set(t) - set(k)
both_cpp_java = set(t) & set(k) - set(h)
both_cpp_python = set(t) & set(h) - set(k)
both_java_python = set(k) & set(h) - set(t)
all_three = set(t) & set(k) & set(h)

print("Sinh viên chỉ thi ngôn ngữ C++:", only_cpp)
print("Sinh viên chỉ thi ngôn ngữ Java:", only_java)
print("Sinh viên chỉ thi ngôn ngữ Python:", only_python)
print("Sinh viên thi cả C++ và Java:", both_cpp_java)
print("Sinh viên thi cả C++ và Python:", both_cpp_python)
print("Sinh viên thi cả Java và Python:", both_java_python)
print("Sinh viên dự thi cả ba ngôn ngữ:", all_three)