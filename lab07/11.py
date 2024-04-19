n = int(input("Nhập tổng số sinh viên: "))
a = int(input("Nhập số lượng sinh viên dự thi ngôn ngữ C++: "))
b = int(input("Nhập số lượng sinh viên dự thi ngôn ngữ Java: "))
c = int(input("Nhập số lượng sinh viên dự thi ngôn ngữ Python: "))
cpp = [int(input(f"Nhập số thứ tự sinh viên C++ {i+1}: ")) for i in range(a)]
java = [int(input(f"Nhập số thứ tự sinh viên Java {i+1}: ")) for i in range(b)]
python = [int(input(f"Nhập số thứ tự sinh viên Python {i+1}: ")) for i in range(c)]
single_language_students = set(cpp + java+ python)
two_languages_students = set(cpp).intersection(java) | \
                          set(cpp).intersection(python) | \
                          set(java).intersection(python)
three_languages_students = set(cpp).intersection(java).intersection(python)

# In ra danh sách các sinh viên
print("Sinh viên chỉ dự thi một ngôn ngữ:", single_language_students)
print("Sinh viên dự thi trên hai ngôn ngữ:", two_languages_students)
print("Sinh viên dự thi trên ba ngôn ngữ:", three_languages_students)
