#Yeu cau : sinh list bieu dien ma tran don vi bac n
n=int(input("Nhap kich co ma tran A:"))

a=[]

for i in range(n):
    row=[0] * n #Khoi tao mot hang voi cac phan tu bang 0
    row[i] = 1 #Dat gia tri 1 cho duong cheo chinh
    a.append(tuple(row)) #Them hang vao day A

for row in a:
    print(row)