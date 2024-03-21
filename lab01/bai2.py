s = int(input("Nhập số giây :"))
m = int(input("Nhập số phút:"))
h = int(input("Nhập số giờ:"))
d = int(input("Nhập số ngày:"))
ket_qua=d*24*60*60 + h*60*60 + m*60 + s
print("Tổng số giây là:",ket_qua)