n = int(input("Nhap vao so tu nhien n: "))
while n <= 0:
    n = int(input("Day khong phai la so tu nhien, vui long nhap lai: "))
nguyen_to = []
i = 2 
while len(nguyen_to) < n:
    is_nguyento = True
    for j in range(2, int(i ** 0.5)+1):
        if i % j == 0:
            is_nguyento = False
            break
    if is_nguyento:
        nguyen_to.append(i)
    i += 1
print("Day",n,"so nguyen to dau tien la: ", nguyen_to)
        