def cong_tru_nhan_chia(a,b):
    cong= a+b
    tru=a-b
    nhan=a*b
    chia=a/b
    return("cong:", cong, "tru:", tru, "nhan:", nhan, "chia:", chia)
a=int(input("nhap so : "))
b=int(input("nhap so: "))
print(cong_tru_nhan_chia(a,b))