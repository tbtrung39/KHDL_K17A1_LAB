m = set(str(int(input("Nhap so tu nhien m:"))))
n = set(str(int(input("Nhap so tu nhien n:"))))

#tinh tong cac chu so chung
tap_hop_chung = m.intersection(n)
tong=0
for i in tap_hop_chung:
    tong += int(i)

print("Tong cac chu so chung cua m va n la:",tong)