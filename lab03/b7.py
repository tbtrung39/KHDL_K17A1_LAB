tong_ngich_dao = int(input("Nhập tổng số nghịch đảo là:"))
S = 0
for i in range (1,tong_ngich_dao+1):
    S += 1/i
print("Tổng các số nghịch đảo là:",S)