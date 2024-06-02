import csv
with open(file =r"lab11\bai5\Phieu_Diem.txt", mode = "r") as f:
    phieu_diem = csv.reader(f)
    phieu_diem = list(phieu_diem)
with open(file =r"lab11\bai5\Sbd_Ph.dat", mode = "r") as f:
    sbd = csv.reader(f)
    sbd = list(sbd)

with open(file =r"lab11\bai5\Sbd_Ten.txt", mode = "r") as f:
    ten= csv.reader(f)
    ten= list(ten)

danh_sach = []
for i in phieu_diem:
    lst=[]
    for j in sbd:
        if i[0] == j[1]:
            for k in ten:
                if k[0]==j[0]:
                    lst.append(j[0])
                    lst.append(k[1])
                    lst.append(i[1])
                    danh_sach.append(lst)
with open(file =r"lab11\bai5\ketqua.txt", mode = "w") as f:
    write = csv.writer(f)
    sorted = sorted(danh_sach,key=lambda x: int(x[2]), reverse = True)
    for i in sorted:
        write.writerow(i)
