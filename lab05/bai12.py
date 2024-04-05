str = input("Nhập chuỗi ký tự: ")
str1 = str.replace(",", "").replace(" ", "")

tu = str1.split()

print("Các từ trong chuỗi:", ",".join(tu))

