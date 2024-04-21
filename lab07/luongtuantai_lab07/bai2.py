list_N = []
n = int(input("số phần tử  là số tự nhiên của list_N: "))
for i in range(n):
    a = int(input(f"nhập vào phần tử thứ {i  + 1}: "))
    list_N.append(a)
B = set()
B.update(list_N)
print(B)