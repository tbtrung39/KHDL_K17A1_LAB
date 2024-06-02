with open("lab11/bai1/dayso.dat", mode="r", encoding="utf-8") as file:
       read_file = file.readline().strip().split(',')
       list_dayso = list(map(int, filter(None, read_file)))
total = 0
print(list_dayso)
for i in list_dayso:
       print(i, end=" ")
       if i % 2 != 0:
              total += i
print("\n")
print(f"Tổng các số hạng lẻ trong dãy là: {total}")
