while True:
    tu_so = int(input("Nhập tử số: "))
    mau_so = int(input("Nhập mẫu số: "))
    if mau_so != 0:
        break
    else:
        print("Nhập lại")
print(f"Phân số được nhập là {tu_so/mau_so}")
