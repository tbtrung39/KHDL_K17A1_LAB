lisst = []
while True : 
    so_tn = input("Nhap vao so tu nhien : ")
    lisst.append(so_tn)
    if so_tn == "0" : 
        break
# chuyen cac phan tu duong len dau và in ra danh sach : 
ptu_duong = [i for i in lisst if i > "0"]
ptu_conlai = [i for i in lisst if i <= "0" ]
danh_sach = ptu_duong + ptu_conlai
print("danh sach duoc thay doi la : ", danh_sach)
#  chen so vao dau, cuoi, vitri 5 :
m = input("Nhap mot so de chen : ")
lisst.insert(0, m)
lisst.append(m)
if len(lisst) >= 5 : 
    lisst.insert(5, m)
else: 
    print("danh sach khong du 5 gia tri de chen !!!")

print("danh sach sau khi chen : ", lisst)