so = int(input("nhập số nguyên:"))
if so < 1000 and so >=100:
    so_hang_tram = so // 100
    so_hang_chuc = (so//10)%10
    so_hang_don_vi = (so//1)%10
    print(f"{so_hang_tram}trăm,{so_hang_chuc}chục,{so_hang_don_vi}đơn vị")
else:
    print("vui lòng nhập số có 3 chữ số")