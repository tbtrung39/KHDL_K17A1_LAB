n = int(input("nhap so n: "))
A = [[0]*n for _ in range(n)]
for i in range(n):
    A[i][i] = 1
for hang in A:
    print(hang)