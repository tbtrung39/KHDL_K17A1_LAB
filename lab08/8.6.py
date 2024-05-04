def  ucln ( a , b ):
    while  b  !=  0 :
        a , b  =  b , a  %  b
    return  a
def  bcnn ( a , b ):
    return ( a  *  b ) //  ucln ( a , b )
so_a  =  int ( input ( "Nhập số a: " ))
so_b  =  int ( input ( "Nhập số b: " ))
ket_qua  =  bcnn ( so_a , so_b )
print ( "Bội chung nhỏ nhất của" , so_a , "và" , so_b , "là:" , ket_qua )