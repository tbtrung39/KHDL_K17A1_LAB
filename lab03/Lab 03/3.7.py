'''
Viết chương trình tính tổng nghịch đảo của n số nguyên đầu tiên.
Ví dụ: S=1 + 1/2 + 1/3 +…+ 1/n
'''
n=int(input("Nhap so nguyen duong n: "))
gia_tri_ban_dau=0
for i in range(1,n+1):
    gia_tri_ban_dau += 1/i
print("Tong nghich dao cua",n, "so nguyen dau tien la:",gia_tri_ban_dau)