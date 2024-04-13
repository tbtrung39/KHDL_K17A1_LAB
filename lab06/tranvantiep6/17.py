n = int(input("Nhap bac n : "))
matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
for a in matrix : 
    print(a)