#6
n=int(input("moi nhap so nguyen n:"))
count=0
so_hien_tai=2
while count < n:
    la_so_nguyen_to=True
    for i in range(2,int(so_hien_tai**0.5)+1):
        if so_hien_tai%i==0:
            la_so_nguyen_to=False
            break
    if la_so_nguyen_to:
        print(so_hien_tai,end='')
        count+=1
    so_hien_tai+=1