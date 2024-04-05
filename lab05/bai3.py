n =int(input("nhập số tự nhiên n: "))
chuoi_nhi_phan=''
if n ==0:
    chuoi_nhi_phan='0'
while n>0:
    chuoi_nhi_phan= str(n%2)+chuoi_nhi_phan
    n//=2
print("chuỗi nhị phân là:", chuoi_nhi_phan)