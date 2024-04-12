lst = []
while True:
    n = int(input("Nhap cac so tu nhienn, nhap 0 de ket thuc: "))
    if n == 0:
        break
    lst.append(n)
print("Danh sach ban dau: ", lst)
lst = [1, 2, 3] + lst + [1, 2, 3]
lst.insert(4, 1)
print("Danh sach sau khi chen la: ", lst)
k = int(input("Nhap vi tri cua phan tu can xoa: "))
del lst[k - 1]
print("Danh sach sau khi xoa phan tu thu", k, ":", lst)
sorted_lst_tang_dan = sorted(lst)
print("Danh sach sau khi sap xep tang dan: ", sorted_lst_tang_dan)
sorted_lst_giam_dan = sorted(lst)
print("Danh sach sau khi sap xep giam dan: ", sorted_lst_giam_dan)