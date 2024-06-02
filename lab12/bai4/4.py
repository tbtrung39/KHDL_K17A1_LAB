import csv
try:
    with open(file =r"lab12\bai4\vao.txt",mode = "r") as file:
        read_file = csv.reader(file)
        lst= list(read_file)
    with open(file = r"lab12\bai4\xuat.txt",mode = "w") as doc:
        write_doc = csv.writer(doc)
        for i in lst:
            write_doc.writerow(i)
except Exception as e:
    print(e)
