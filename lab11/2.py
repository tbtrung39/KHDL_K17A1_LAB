with open("lab11/bai2/Inp.txt", mode="r", encoding="utf-8") as file_Inp:
    list_dayso = [int(num) for num in file_Inp.readline().strip().split(',')]

list_sort_dayso = sorted(list_dayso)

with open("lab11/bai2/Out.txt", mode="w") as file_Out:
    file_Out.write(",".join(map(str, list_sort_dayso)))
