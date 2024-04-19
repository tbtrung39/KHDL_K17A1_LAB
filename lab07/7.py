A = set()
B = set()
n = int(input("So phan tu cua tap A và B: "))
for i in range(n):
    ptua = input(f"Nhap vao phan tu thu {i +1} cua A: ")
    ptub = input(f"Nhap vao phan tu thu {i +1} cua B: ")
    A.add(ptua)
    B.add(ptub)
print(A.intersection(B))
    