str=input("nhap chuoi nhi phan: ")
nhi_phan=True
for i in str:
    if i !='0' and i!= '1':
        nhi_phan=False
        break
if nhi_phan:
    thap_phan=0
    for i in range (len(str)):
        thap_phan +=int(str[1])*(2**(len(str)-i-1))
    print("so thap phan tuong ung la:", thap_phan)
else:
    print("chuoi ky tu khong phai la chuoi nhi phan")