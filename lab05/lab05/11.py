chuoi=input("Nhap chuoi ki tu nhi phan:")

nhi_phan=True

for char in chuoi:
    if char != "0" and char != "1":
        nhi_phan=False
        break
if nhi_phan:
    thap_phan=0
    for i in range(len(chuoi)):
        thap_phan += int(chuoi[i])*(2**(len(chuoi)-i-1))
    print("So thap phan tuong ung la:",thap_phan)
else:
    print("Chuoi ki tu khong phai chuoi nhi phan.")
