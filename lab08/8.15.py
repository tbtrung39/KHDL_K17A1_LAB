def  lst_int ():
    lst  = []
    n  =  int ( input ( "Nhap vao so luong nguyen nhap tu ban key: " ))
    for  a  in  range ( n ):
        a  =  int ( input ( f"Nhap vao so nguyen thu { a + 1 } tu ban phim: " ))
        lst . append ( a )
    return  lst
lstbp  =  lst_int ()
Even_n  = [ i  for  i  in  lstbp  if  i  %  2  !=  0 ]
Squared_a  =  list ( map ( lambda  a : a ** 2 , Even_n ))
print ( f"Danh sách các số nguyên nguyen a le sau khi binh phuong la { Squared_a } " )