n=int(input("nhap so tu nhien N :"))
nhi_phan=""
while n<0:
    n=int(input("n la so tu nhien duong .Nhap lai n:"))
while n>0:
    nhi_phan=str(n%2)+nhi_phan
    n//=2
print('N doi tu he 10 sang he 2 la :',nhi_phan)