import csv
with open(file =r"lab11\bai7\m_num.txt",mode = "r") as read:
    read_m = csv.reader(read)
    list_m = list(read_m)
with open(file =r"lab11\bai7\n_num.txt",mode = "r") as readd:
    read_n = csv.reader(readd)
    list_n = list(read_n)
s= []
for i in list_m[0][::]:
    for j in list_n[0][::]:
        if i == j:
            s.append(i)
with open(file = r"lab11\bai7\so_chung.txt",mode ="w") as file:
    write = csv.writer(file)
    write.writerow(s)
