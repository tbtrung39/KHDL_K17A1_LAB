so = int(input("Nhập số n: "))
a = 0

print(so, "đọc thành chữ là")
while so != 0:
    a = (a * 10) + (so % 10)
    so //= 10
while a != 0:
    if a % 10 == 0:
        print("Không", end=" ")
    elif a % 10 == 1:
        print("Một", end=" ")
    elif a % 10 == 2:
        print("Hai", end=" ")
    elif a % 10 == 3:
        print("Ba", end=" ")
    elif a % 10 == 4:
        print("Bốn", end=" ")
    elif a % 10 == 5:
        print("Năm", end=" ")
    elif a % 10 == 6:
        print("Sáu", end=" ")
    elif a % 10 == 7:
        print("Bảy", end=" ")
    elif a % 10 == 8:
        print("Tám", end=" ")
    elif a % 10 == 9:
        print("Chín", end=" ")

    a //= 10