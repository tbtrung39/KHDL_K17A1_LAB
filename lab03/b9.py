n= int(input("nhap mot so nguyen duong: "))
s4=0
s5=0
s6=0
for i in range(1,n+1):
    s4+=i*i
    s5+=(2*i+1)**3 
    s6+=(2*i)**4
print("s4 =",s4,"s5 =",s5,"s6 =",s6)    