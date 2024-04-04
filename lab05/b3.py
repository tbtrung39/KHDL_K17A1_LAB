n = int(input("nhập một số tự nhiên: "))
chuoi_nhi_phan=""
while n >0:
    chuoi_nhi_phan+=str(n%2)
    n=n//2
print("chuỗi nhị phân là: ",chuoi_nhi_phan)