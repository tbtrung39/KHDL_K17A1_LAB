n=set(str(int(input("nhap vao gia tri n:"))))
m=set(str(int(input("nhap vao gia tri m:"))))
q=m.intersection(n)
tong=0
for i in q:
    tong=tong+int(i)
print(tong)