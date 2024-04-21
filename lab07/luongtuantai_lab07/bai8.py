A = set()
n = int(input("số phần tử của tập A: "))
for i in range(n):
    ptua = (input(f"nhập vào phần tử thứ {i +1} của A: "))
    A.add(ptua)
inter = 0
flt = 0
strings = 0
for j in A:
    if j.isdigit():
        inter += 1
    elif isinstance(j,float):
        flt += 1
    elif isinstance(j,str):
        strings +=1
print(f"số lượng phần tử là số nguyên trong set A là {inter}")
print(f"số lượng phần tử là số thực trong set A là {flt}")
print(f"số lượng phần tử là ký tự trong set A là {strings}")