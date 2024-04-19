n=int(input("nhap so tu nhien n: "))
tap_cac_so_nguyen_to = set()  
dem = 0  
so = 2    
print("Dãy", n, "số nguyên tố đầu tiên là:")
while dem < n:
    la_nguyen_to = True
    for i in range(2, int(so ** 0.5) + 1):
        if so % i == 0:
            la_nguyen_to = False
            break
    if la_nguyen_to:
        tap_cac_so_nguyen_to.add(so)
        dem += 1
    so += 1

print("Các số nguyên tố đã tìm thấy:", tap_cac_so_nguyen_to)