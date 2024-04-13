danh_sach = input("Nhap day so tu nhien : ")
lisst = []
for i in danh_sach : 
    lisst.append(i)
# phan tu lon thu hai va vi tri cua no : 
max_1 = max(lisst)
del_max_1 = lisst.remove(max_1)
max_2 = max(lisst)
lct_max_2 = lisst.index(max_2)
print(f"phan tu lon thu hai la {max_2}, vi tri cua no la {lct_max_2}")
