dct_a=dict()
for i in range(1,101):
    j=i
    nhi_phan=""
    while j > 0:
        so_du = j%2
        nhi_phan=str(so_du)+nhi_phan
        j= j//2
        dct_a.update({i : nhi_phan})
print(dct_a)