def so_lon_nhat(a,b,c):
    max=a
    if b>max: 
        max=b 
    if c>max:
         max=c 
    return max
def so_nho_nhat(a,b,c):
    min=a
    if b<min:
        min=b
    if c<min:
        min=c
    return min
a=int(input("nhap so : "))
b=int(input("nhap so: ")) 
c=int(input("nhap so : "))
print(so_lon_nhat(a,b,c)) 
print(so_nho_nhat(a,b,c))