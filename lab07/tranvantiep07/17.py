tudien = []
a = int(input("Nhap so sinh vien : "))
while len(tudien) <= a : 
    dic = {}
    key1 = "msv"
    key2 = "name"
    key3 = "point"
    msv = int(input("Nhap ma sinh vien (6 ky tu so) : "))
    name = input("Nhap ten sinh vien : ")
    point = round(float(input("Nhap diem so cua sinh vien : ")), 0)
    dic[key1] = msv
    dic[key2] = name
    dic[key3] = point
    tudien.append(dic)
print(tudien)
# sắp xếp : 
n = len(tudien)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if tudien[j]['point'] < tudien[j + 1]['point']:
            tudien[j], tudien[j + 1] = tudien[j + 1], tudien[j]
print("sap xep theo gia tri point giam dan la : ", tudien)