cac_so = []
for i in range (1,101):
    cac_so.append(i)
so_nhi_phan = ""
for i in cac_so:
    so_nhi_phan  = str(i%2) + so_nhi_phan
    i = i//2

for cac_so in enumerate (cac_so,int(so_nhi_phan)):
    print(cac_so)