# Số sinh viên dự thi từng ngôn ngữ
so_sinh_vien_C_plus_plus = 3
so_sinh_vien_Java = 4
so_sinh_vien_Python = 5

# Danh sách sinh viên dự thi từng ngôn ngữ
sinh_vien_C_plus_plus = {1, 2, 3}
sinh_vien_Java = {4, 5, 6, 7}
sinh_vien_Python = {6, 7, 8, 9, 10}

# Danh sách sinh viên chỉ dự thi một ngôn ngữ
chi_C_plus_plus = sinh_vien_C_plus_plus - sinh_vien_Java - sinh_vien_Python
chi_Java = sinh_vien_Java - sinh_vien_C_plus_plus - sinh_vien_Python
chi_Python = sinh_vien_Python - sinh_vien_C_plus_plus - sinh_vien_Java

# Danh sách sinh viên dự thi cả hai ngôn ngữ
C_plus_plus_va_Java = sinh_vien_C_plus_plus & sinh_vien_Java
C_plus_plus_va_Python = sinh_vien_C_plus_plus & sinh_vien_Python
Java_va_Python = sinh_vien_Java & sinh_vien_Python

# Danh sách sinh viên dự thi cả ba ngôn ngữ
tat_ca_ba_ngon_ngu = sinh_vien_C_plus_plus & sinh_vien_Java & sinh_vien_Python

# In kết quả
print("Sinh viên chỉ thi ngôn ngữ C++:", chi_C_plus_plus)
print("Sinh viên chỉ thi ngôn ngữ Java:", chi_Java)
print("Sinh viên chỉ thi ngôn ngữ Python:", chi_Python)
print("Sinh viên thi cả ngôn ngữ C++ và Java:", C_plus_plus_va_Java)
print("Sinh viên thi cả ngôn ngữ C++ và Python:", C_plus_plus_va_Python)
print("Sinh viên thi cả ngôn ngữ Java và Python:", Java_va_Python)
print("Sinh viên thi cả ba ngôn ngữ:", tat_ca_ba_ngon_ngu)