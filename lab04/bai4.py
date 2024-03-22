#bài 4
tu = int(input("nhập tử số:"))
while True:
    mau = int(input("nhập mẫu số:"))
    if mau == 0 :
        print("vui lòng nhập mẫu số khác 0")
    else:
        print(f"kết quả là:{tu/mau}")
        break