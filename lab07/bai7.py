A = set(input("Nhập tập hợp A (các ký tự chữ và số, cách nhau bằng dấu cách): ").split())
B = set(input("Nhập tập hợp B (các ký tự chữ và số, cách nhau bằng dấu cách): ").split())
pt_chung = A.intersection(B)
print("Các phần tử chung của tập hợp A và tập hợp B là:", pt_chung)
