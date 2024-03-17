a=int(input('nhập thâm niên công tác:'))
if a<12:
    b=2.34
elif a>=12 and a<36:
    b=3.33
elif a>=36 and a<60:
    b=3.66
else:
    b=3.99
c=b*1350000
print('lương nhân viên nhận được là:',c)
    