n=int(input("Nhập n:"))
list_A=[]
for i in range(n):
    hang_ngang=[0]*n
    hang_ngang[i]=1
    list_A.append(hang_ngang)
print("Ma trận bậc",n,"la:")
for hang_ngang in list_A:
    print(hang_ngang)

