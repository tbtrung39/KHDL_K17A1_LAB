str1 = input("Nhap mot doan van ban hoan chinh: ")
a= input("Nhap vao mot tu don: ")
if a.isalpha() and a == a.replace(" ",""):
    print("co", str1.count(a), "tu: ",a)
else:
    print(a, "Khong phai la tu don")
