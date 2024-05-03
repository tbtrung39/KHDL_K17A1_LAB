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

a=int(input("nhap so: "))
b=int(input("nhap so: "))
print(uoc_chung_lon_nhat(a,b))