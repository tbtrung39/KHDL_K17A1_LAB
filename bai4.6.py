chuoi = ""
n = int(input("Nhập số: "))
so_nguyen = n
while so_nguyen != 0:
    du = so_nguyen % 10
    so_nguyen //= 10
    if du == 0:
        chuoi = "Không " + chuoi
    elif du == 1:
        chuoi = "Một " + chuoi
    elif du == 2:
        chuoi = "Hai " + chuoi
    elif du == 3:
        chuoi = "Ba " + chuoi
    elif du == 4:
        chuoi = "Bốn " + chuoi
    elif du == 5:
        chuoi = "Năm " + chuoi
    elif du == 6:
        chuoi = "Sáu " + chuoi
    elif du == 7:
        chuoi = "Bảy " + chuoi
    elif du == 8:
        chuoi = "Tám " + chuoi
    else:
        chuoi = "Chín " + chuoi
print(f"Số {n} được đọc là: \n{chuoi}")