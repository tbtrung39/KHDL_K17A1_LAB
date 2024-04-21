numbers = {}
while True:
    num = input("Nhap so tu nhien(enter de ket thuc) la:")
    if num == "":
        break
    try:
        nums = int(num)
        if num < 0:
            print("vui long nhap so tu nhien duong !!!")
        else:
            numbers[num] = None
    except ValueError:
        print("Vui long nhap so hop le !!!")
print("Danh sach la:",set(numbers))
