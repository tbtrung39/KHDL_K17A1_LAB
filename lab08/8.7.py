def  find_min_max ( num1 , num2 , num3 ):
    min_num  =  min ( num1 , num2 , num3 )
    max_num  =  max ( num1 , num2 , num3 )
    return  min_num , max_num
num1  =  int ( input ( "Nhập số thứ nhất: " ))
num2  =  int ( input ( "Nhập số thứ hai: " ))
num3  =  int ( input ( "Nhập số ba: " ))
min_num , max_num  =  find_min_max ( num1 , num2 , num3 )
print ( "Số nhỏ nhất là:" , min_num )
print ( "Số lớn nhất là:" , max_num )