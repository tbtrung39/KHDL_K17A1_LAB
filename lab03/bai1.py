n=int(input("nhập số tự nhiên n: "))
tong =1
tu_so=2
mau_so=3
for i in range(1,n+1):
    tong+=(tu_so/mau_so)
    tu_so*=(2*i)
    mau_so*=(2*i+1)
print(f"Đáp án là = {tong:.3f}")