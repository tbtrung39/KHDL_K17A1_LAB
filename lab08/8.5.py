def  tim_uoc_chung_lon_nhat ( a , b ):
    while  b  !=  0 :
        a , b  =  b , a  %  b
    return  a
a  =  int ( input ( "Nhập số thứ nhất: " ))
b  =  int ( input ( "Nhập số thứ hai: " ))
ucln  =  tim_uoc_chung_lon_nhat ( a , b )
print ( f"Ước chung lớn nhất của { a } và { b } là: { ucln } " )