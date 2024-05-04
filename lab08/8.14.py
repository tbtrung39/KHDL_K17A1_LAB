def lst_int ():
    lst  = []
    n  =  int(input( "Nhap vao so luong nguyen nhap tu ban key: " ))
    for a in range( n ):
        a  =  int(input (f"Nhap vao so nguyen thu {a +1} tu ban phim: " ))
        lst . append( a )
    return lst
lstbp  =  lst_int ()
Squared_a =  list ( map ( lambda  a : a ** 2 , lstbp ))
print ( f"Danh sách các số nguyen a sau khi bình phương la { Squared_a } " )