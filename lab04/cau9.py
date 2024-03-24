n = int(input("Nhap vao mot gia tri n: "))
tong = 0 
while n > 0:
    chu_so = n % 10
    tong = tong + chu_so
    n = n // 10
print("Tong cac chu so da nhap la: ", tong)