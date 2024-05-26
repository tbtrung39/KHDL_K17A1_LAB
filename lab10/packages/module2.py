import math
import random
def dayso(n):
    random_numbers = [random.randint(1,100) for _ in range(n)]
    return random_numbers

def snto(n):
    if n <= 1:
        return False
    for i in range (2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True
def snto_chia_cho7(n):
    return snto(n) % 7 == 0
    
def tong():
    random_numbers = [x for x in range(101) if x % 2 == 1]
    s = sum(random_numbers)
    return s

def nhapdulieu(a,n):
    for i in range(n):
        print('Chuẩn bị nhập ma trận hàng thứ',i+1,': ')
        b=[]
        for j in range(n):
            x=int(input('Nhập phần tử cột thứ '+str(j+1)+': '))
            b=b+[x]
        a.append(b)
def in_ma_tran(a,n):    
    for i in range(n):
        for j in range(n):
            print(a[i][j],end=' ')
        print()
def mt_chuyen_vi(a,n):
    at=[[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            at[i][j]=a[j][i]
    return at
def kiem_tra_doi_xung(a,n):
    if mt_chuyen_vi(a,n)==a:
        return True
    else:
        return False