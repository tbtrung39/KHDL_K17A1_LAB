import csv
with open(file = r"lab11\bai6\matran.txt",mode = "r") as f:
    filedata = csv.reader(f)
    list_item = list(filedata)
    print(list_item[0])
    print(list_item[2])
    print(list_item)
    odd = []
    for i in list_item:
        b=[]
        for s in i:
            if int(s) %2 !=0:
                b.append(s)
            else:
                b.append(0)
        if len(b)<4:
            for i in range(4-len(b)):
                b.append(0)
        odd.append(b)
with open(file = r"lab11\bai6\ODD.txt",mode = "w",newline="") as writer:
    writer_file = csv.writer(writer)
    for i in odd:
        writer_file.writerow(i)
#d
with open(file = r"lab11\bai6\ODD.txt",mode = "r") as read:
    read_file = csv.reader(read)
    list_item = list(read_file)
    print("dong cuoi file ODD.txt la:",list_item[-1])