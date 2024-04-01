Str = input("Nhập chuỗi ký tự: ")
tu_trong_Str = Str.split()
for tu in tu_trong_Str:
    tu=tu.strip(",")
    print(tu)
