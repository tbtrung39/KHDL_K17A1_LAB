def  la_so_nguyen_to ( x ):
    if  x  <=  1 :
        return  False
    for  i  in  range ( 2 , int ( x  **  0.5 ) +  1 ):
        if  x  %  i  ==  0 :
            return  False
    return  True
def  in_so_nguyen_to ( n ):
    print ( f" Các số nguyên tố nhỏ hơn { n } :" )
    for  i  in  range ( 2 , n ):
        if  la_so_nguyen_to ( i ):
            print ( i , end = " " )
n  =  int ( input ( "Nhập số n: " ))
in_so_nguyen_to ( n )