n = int(input("Nhập vào 1 số nguyên: "))

if n < 100 or n> 999:
    print(0)
else:
    so_hang_tram = n // 100
    print("số hàng trăm của chữ số đó là",so_hang_tram)