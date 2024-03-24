'''
Viết chương trình tính kết quả của phép toán sau 
(làm tròn 3 chữ số thập phân):
1 + 2/3 + 2/3 x 4/5 + 2/3 x 4/5 x 6/7 + ... +
+ 2/3 x 4/5 x 6/7 x 8/9 x ... x 2(n+1)/(2n+3)
'''
n = int(input("Nhap gia tri cua n: "))
ket_qua = 1
tich_bieu_thuc = 1
for i in range(1, n+1):
    tich_bieu_thuc *=(2*i)/((2*i)+1)
    ket_qua += tich_bieu_thuc
print("Ket qua cua bieu thuc la: ",round(ket_qua,3))