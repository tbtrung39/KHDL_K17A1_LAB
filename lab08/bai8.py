import math
def tinh(a):
    chuvi=2*math.pi*a
    dientich=math.pi*a**2
    return chuvi,dientich
a=float(input("nhap ban kinh hinh tron :  "))
chuvi,dientich=tinh(a)
print("chu vi =  ",chuvi)
print("dien tich = ",dientich)