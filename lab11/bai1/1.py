import csv
with open(file =r"lab11\bai1\dayso.dat",mode="r") as dayso:
       read = csv.reader(dayso)
       list_dayso = list(read)
S = 0
for i in list_dayso[0][::]:
       if int(i)%2!=0:
              S+=int(i)
print("Tổng các số hạng lẻ trong dãy là:",S)