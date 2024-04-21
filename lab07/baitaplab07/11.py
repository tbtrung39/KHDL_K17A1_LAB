a_students = [1, 2, 3, 4, 5]
b_students = [2, 4, 6, 8, 10]
c_students = [3, 6, 9, 12, 15]
a_set = set(a_students)
b_set = set(b_students)
c_set = set(c_students)
print(a_set)
print(b_set)
print(c_set)
only_cpp = a_set - b_set - c_set
only_java = b_set - a_set - c_set
only_python = c_set - a_set - b_set

cpp_and_java = a_set & b_set - c_set
cpp_and_python = a_set & c_set - b_set
java_and_python = b_set & c_set - a_set

all_three = a_set & b_set & c_set
print("only c++:",only_cpp)
print("only_java:",only_java)
print("only python:",only_python)
print("cpp and java:",cpp_and_java)
print("cpp and python:",cpp_and_python)
print("java and python:",java_and_python)
print("all:",all_three)
