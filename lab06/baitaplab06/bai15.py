n = int(input("Enter a number: "))
danh_sach = []
for i in range(n):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    score = float(input("Enter score: "))
    danh_sach.append((name, age, score))
danh_sach_sap_xep = sorted(danh_sach)
print("the list after arrangement:")
for item in danh_sach_sap_xep:
    print(item)