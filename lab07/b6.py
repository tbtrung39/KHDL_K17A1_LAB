n = int(input("Nhap so nguyen duong la:"))
nguyen_to = {}
so_hien_tai = 2
vi_tri = 1
while len(nguyen_to) < n:
    la_so_nto = True
    for i in range(2,int(so_hien_tai**0.5)+1):
        if so_hien_tai % i ==0:
            la_so_nto = False
            break
    if la_so_nto:
        nguyen_to[vi_tri] = so_hien_tai
        vi_tri += 1
    so_hien_tai += 1
print(f"Day {n} la so nguyen to dau tien:")
for vi_tri in nguyen_to:
    print(f"{vi_tri}:{nguyen_to[vi_tri]}")