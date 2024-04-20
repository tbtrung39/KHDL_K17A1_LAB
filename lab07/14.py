tu_dien_nhi_phan={}
for i in range(1,101):
  tu_dien_nhi_phan[i]=bin(i)[2:]
for so,nhi_phan in tu_dien_nhi_phan.items():
  print(f"{so} tuong ung voi nhi phan:{nhi_phan}")