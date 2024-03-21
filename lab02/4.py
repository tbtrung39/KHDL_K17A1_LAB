so = int(input("nhap so nguyen:"))
so_hang_tram = (so//100)%10
if so_hang_tram == 0:
    print("0")
else:
    print("so hang tram la",so_hang_tram)