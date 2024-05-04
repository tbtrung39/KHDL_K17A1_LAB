def  cong ( a , b ):
    return  a  +  b
def  tru ( a , b ):
    return  a  -  b
def  nhan ( a , b ):
    return  a  *  b
def  chia ( a , b ):
    if  b  ==  0 :
        return  "Không thể chia cho 0"
    else :
        return  a  /  b
a  =  float ( input ( "Nhập số a: " ))
b  =  float ( input ( "Nhập số b: " ))
print ( "Tổng của a và b là:" , cong ( a , b ))
print ( "Hiệu của a và b là:" , tru ( a , b ))
print ( " Tích của a và b là:" , nhan ( a , b ))
print ( "Thương của a và b là:" , chia ( a , b ))