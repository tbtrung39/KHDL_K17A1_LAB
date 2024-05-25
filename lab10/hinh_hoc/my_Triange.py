import math
def is_tam_giac(a,b,c):
    if (a+b>c) and (a+c>b) and (b+c>a):
        return True
    else:
        return False

def chu_vi_tam_giac(a,b,c):
    if (a+b>c) and (a+c>b) and (b+c>a):
        chu_vi=a=b+c
        print(chu_vi)
    else:
        print("khong co")

def S_tam_giac(a,b,c):
    chu_vi=a+b+c
    if (a+b>c) and (a+c>b) and (b+c>a):
        dien_tich=math.sqrt(chu_vi*(chu_vi-a)+(chu_vi-b)+(chu_vi-c))
        print (dien_tich)
    else:
        print("khong co")