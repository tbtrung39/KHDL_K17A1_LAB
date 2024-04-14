x=int(input("nhap so hang:"))
y=int(input("nhap so cot:"))
ma_tran=[]
for i in range(0,x):
    row=[]
    for j in range(0,y):
        row.append(i*j)
    ma_tran.append(row)
print("Ma tran hai chieu:",ma_tran)
