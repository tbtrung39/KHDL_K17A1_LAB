lisst = []
while True : 
    so_tn = input("Nhap vao so tu nhien : ")
    lisst.append(so_tn)
    if so_tn == "0" : 
        break
# chen danh sach vao cac vi tri nhu yeu cau : 
danh_sach = [1,2,3]
lisst.insert(0, danh_sach)
lisst.append(danh_sach)
if len(lisst) >= 5 : 
    lisst.insert(5, danh_sach)
else: 
    print("danh sach khong du 5 gia tri de chen !!!")

print("danh sach sau khi chen : ", lisst)
# # xoa phan tu thu k trong danh sach : 
k = int(input("Nhap vi tri phan tu muon xoa "))
ptu_k = lisst[k]
print("danh sach sau khi xoa phan tu k : ", lisst.remove(ptu_k))
# sap xep danh sach theo thứ tu tang dan va giam dan : 
lisst.sort()
print("sap xep theo thu tu tang la : ", lisst)
lisst.reverse()
print("sap xep theo thu tu giam la : ", lisst)
