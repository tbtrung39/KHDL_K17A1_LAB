def uoc_chung_lon_nhat(x,y):
    if x!=0 and y==0:
        ucln=abs(x) 
        return ucln
    else:
        if x==0 and y!=0:  
            ucln=abs(y) 
            return ucln
        else:
            if x<y: min=x 
            else: min=y 
            for i in range(1,min+1): 
                if x%i==0 and y%i ==0: 
                    ucln =i 
            return ucln
def rut_gon(x,y):
    if x==0:
        return ('0/0')
    elif y!=0: 
        return x/uoc_chung_lon_nhat(x,y),"/",y/uoc_chung_lon_nhat(x,y)
    else: 
        return("lo1 1111")
x=int(input("nhap_tu_so:")) 
y=int(input("nhap_mau_so:"))
print(rut_gon(x,y))