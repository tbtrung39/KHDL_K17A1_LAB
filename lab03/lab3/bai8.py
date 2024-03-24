n =  int(input('nhập số n : '))
s4 =0
s5 =0
s6 =0
for i in range(1,n+1):
    s4 += i**2
for j in range(1,n+1,2):
    s5 += j**3
for k in range(0,n+1,2):
    s6 += k**4

print('S4 = ',s4,'S5 = ',s5,'S6 = ',s6)