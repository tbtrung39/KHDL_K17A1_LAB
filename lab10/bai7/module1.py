import random
def sinh_day_so():
    day_so =[random.randint(1,100) for _ in range(100)]
    return day_so
def so_nguyen_to(n):
    for i in range(2,n):
        if n%i ==0:
            return False
    else:
        return True
def snt_chia_het_7(day_so):
    lst=[]
    for i in day_so:
        if so_nguyen_to(i):
            lst.append(i)
    print("cac so nguyen to chia het cho 7 la:",lst)
    return lst
def tong_so_le(a):
    s=0
    for i in a:
        if i %2 != 0:
            s+=i
    print("tong so le la:",s)
    return s
def so_chinh_phuong(x):
    for i in range(1,x):
        if i*i == x:
            return True
    return False
def kiem_tra_chinh_phuong(day_so):
    lst = []
    for i in day_so:
        if so_chinh_phuong(i):
            lst.append(i)
    if lst != []:
        print("cac so chinh phuong trong day la:",lst)
        return lst
    else:
        print("khong co so chinh phuong trong day")
        return