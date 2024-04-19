n = int(input("Nhap tu ban phim: "))
ls1 = [int(i) for i in range(1, n+1)]
ls2 = input("Nhap ten: ").split(",")
dict={}
for i in range(len(ls1)):
    if i<len(ls2):
        dict[ls1[i]] = ls2[i]
print(dict)