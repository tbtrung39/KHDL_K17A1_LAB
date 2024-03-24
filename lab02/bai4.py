n = int(input("Nhập vào số cần xét: "))
a = n /100
if a % 100 >= 1:
    print(f"chữ số hàng trăm của số đó là {a:.0f}")
else:
    print("0")