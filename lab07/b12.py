n=int(input("nhap vao mot so nguyen: "))
dct_a=dict()
for i in range(1,n+1):
    dct_a.update({i : i*i})
print(dct_a)