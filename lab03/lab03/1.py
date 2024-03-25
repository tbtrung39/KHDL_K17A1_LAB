n=int(input("Nhậpp số nguyên n:"))
for i in range(0,n+1):
    tong=0    
    T=2/3*(2*(i+1)/(2*i+3))
    tong+=T
    S=1+2/3+tong
print(f"Gtrị bthức = {S:.3f}")