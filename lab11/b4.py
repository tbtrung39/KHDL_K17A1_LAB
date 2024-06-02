import csv
def uoc(x):
    s=[]
    for i in range(1,x):
        if x%i ==0:
            s.append(i)
    return s
with open(file =r"lab11/f_in.dat", mode = "r") as f:
    read = csv.reader(f)
    list_f = list(read)
    lst = []
    for i in list_f:
        for j in i:
           lst.append(uoc(int(j)))
with open(file =r"lab11/f_out.dat", mode = "w") as file:
    writer = csv.writer(file)
    for i in lst:
        writer.writerow(i)