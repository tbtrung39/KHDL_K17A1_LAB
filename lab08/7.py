# 7
def min_max(a,b,c):
    min_numbers=min(a,b,c)
    max_numbers=max(a,b,c)
    return min_numbers,max_numbers
so_1=int(input("moi nhap so nguyen 1"))
so_2=int(input("moi nhap so nguyen 2"))
so_3=int(input("moi nhap so nguyen 3"))
so_nn,so_ln=min_max(so_1,so_2,so_3)
print("so nho nnat va so lon nhat la:",so_nn,so_ln)