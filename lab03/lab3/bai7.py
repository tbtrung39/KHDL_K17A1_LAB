n=int(input("Nhập số nguyên dương n: "))

gia_tri_ban_dau=0

for i in range(1,n+1) :
    gia_tri_ban_dau += 1/i

print(f"Tổng nghịch đảo của {n} số nguyên đầu tiên là:{gia_tri_ban_dau}")