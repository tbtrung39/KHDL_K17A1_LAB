dct_a=dict()
for i in range(1,101):
    j=i
    thap_phan=""
    while j >0:
        so_du=j%2
        thap_phan=str(so_du) + thap_phan
        j = j //2
        dct_a.update({i : thap_phan})
print(dct_a)