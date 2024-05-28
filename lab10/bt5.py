from packages import in_ra,cs01,cs8p,cs16p
n = int(input("Nhập vào số nguyên n: "))
in_ra(n)
print(f"n sau khi chuyển qua hệ nhị phân là: {cs01(n)}")
print(f"n sau khi chuyển qua hệ bát phân là: {cs8p(n)}")
print(f"n sau khi chuyển qua hệ thập lục phân là: {cs16p(n)}")