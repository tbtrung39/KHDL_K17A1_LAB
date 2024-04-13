n = int(input("nhap so n:"))
list_a = []
for i in range(n):
    hang_ngang = [0]*n
    hang_ngang[i]=1
    list_a.append(hang_ngang)
    print("ma tra bac",n,"la:")
    for hang_ngang in list_a:
        print(hang_ngang)