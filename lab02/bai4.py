a=int(input("nhập vào 1 số nguyên : "))
if a>=100:
    xet_hang_tram=(a//100)%10
    print(f"chữ số hàng trăm của số {a} là {xet_hang_tram}")
else:
    print(f"{0}")