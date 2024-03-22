n=int(input('Nhap so nguyen bat ki :'))
if n<100:
    print(f'Chữ số hàng trăm của số {n} là : 0')
else:
    hang_tram = (n//100) % 10
    print(f"Chữ số hàng trăm của số {n} là: {hang_tram}")