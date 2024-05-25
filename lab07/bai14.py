dct_nhi_phan={}
n=int(input("nhap so n: "))
for i in range(1,n):
    chuoi_nhi_phan=''
    num=i
    while num>0:
        chuoi_nhi_phan=str(num%2)+chuoi_nhi_phan
        num//=2
        dct_nhi_phan[i]=chuoi_nhi_phan
print(dct_nhi_phan)