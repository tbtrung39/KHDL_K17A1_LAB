import random
so_chia_het_5_va_7=[]
for i in range(200):
    if i % 5 ==0 and i%7==0:
        so_chia_het_5_va_7.append(i)
so_ngau_nhien=random.choice(so_chia_het_5_va_7)
print("so ngau nhien chia het cho 5 va 7 duoi 200 la:", so_ngau_nhien)