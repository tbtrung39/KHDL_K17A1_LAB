so=[]
for i in range(1,101):
    so.append(i)
so_nhi_phan=""
for i in so:
    so_nhi_phan= str(i%2) + so_nhi_phan
    i = i//2

for so in enumerate(so,int(so_nhi_phan)):
    print(so)