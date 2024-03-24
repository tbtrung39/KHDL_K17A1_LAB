tnct =  int(input('nhập hệ số lương ở đây : '))
if 0<tnct :
    if tnct <12:
        const = 2.34
    elif 12<= tnct <36:
        const =3.33
    elif 36<= tnct< 60:
        const  =  3.66
    elif tnct >=60:
        const =3.99
    
else:
    print('hệ số lương k  hợp lệ ')
 

print('lương của nhân viên có hệ số lương '
      ,const,'là :',const*1350000,'đòng')