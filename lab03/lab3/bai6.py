n= int(input ("Nhập số nguyên dương n: "))

gia_tri_ban_dau=0

for i in range(1, n+1):
    gia_tri_ban_dau +=  i**3

print (f" Tổng bậc ba của {n} số nguyên đầu tiên là: {gia_tri_ban_dau}")
