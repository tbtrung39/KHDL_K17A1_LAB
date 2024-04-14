n = int(input("so phan tu muon nhap la:"))
lst= []
i =1
while i <=n:
    so_tu_nhien= int(input("Nhap vao mot so tu nhien: "))
    lst.append(so_tu_nhien)
    i+=1
lst_copy= lst.copy()
phan_tu = lst_copy.pop(lst_copy.index(max(lst_copy)))
max_thu_hai = lst.index(max(lst_copy))
print(lst)
print("phan tu lon thu 2 trong list la:",lst[max_thu_hai])
print("vi tri phan tu lon thu 2 la:",max_thu_hai)

max_count = 0
count = 0
s=0
s_max = 0
for num in lst:
    if num>0:
        count+=1
        s+=num
        if s >s_max:
            s_max =s
            max_count = count
    else:
        count =0
        s=0

print("so luong cac so duong lein tiep nhieu nhat la:",max_count)
print("tpmg cac sp dipmg lien  tiep nhieu nhat la:",s_max)