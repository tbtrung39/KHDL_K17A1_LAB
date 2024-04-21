A = set()
B = set()
n = int(input("số phần tử của tập A và B: "))
for i in range(n):
    ptua = (input(f"nhập vào phần tử thứ {i +1} của A: "))
    ptub = (input(f"nhập vào phần tử thứ {i +1} của B: "))
    A.add(ptua)
    B.add(ptub)
print(A.intersection(B))