n = int(input("Nhap vao mot gia tri n: "))
s= 0 
while n > 0:
    chu_so = n % 10
    s+=chu_so
    n = n // 10
print("Tong cac chu so: ",s)