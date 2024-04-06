str = input("nhap chuoi he nhi phan la:")
nhi_phan = True
for c in str:
    if c != '0' and c != '1':
        nhi_phan = False
        break
if nhi_phan:
    doi_he_tp = 0
    for i in range(len(str)):
        doi_he_tp += int(str[i])*(2**(len(str)-i-1)) 
    print("So thap phan tuong ung voi he nhi phan la:",doi_he_tp)
else:
    print("Chuoi nhi phan nhap vao ban phim khong hop le !!!")