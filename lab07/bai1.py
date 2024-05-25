import msvcrt  
tap_hop = set()
print("nhap cac phan tu (an 'ESC' de ket thuc):")
while True:
    if msvcrt.kbhit():
        ky_tu = msvcrt.getch().decode()
        if ky_tu == '\x1b':  
            break
        elif ky_tu.isdigit():
            print("ky tu khong hop le!!!")
        else:
            tap_hop.add(ky_tu)

print(tap_hop)
