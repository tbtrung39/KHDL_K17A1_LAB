while True:
    n = int(input("Nhập số nguyên dương (nhập số âm để kết thúc): "))
    if n < 0:
        print("Chương trình kết thúc.")
        break
    print(f"Số nguyên dương bạn vừa nhập là: {n}")
