def  nv ():
    n  =  input ( "Nhập vào mười nhân viên: " )
    qq  =  input ( "Nhap vao que quan cua nhan vien: " )
    tn  =  int ( input ( f"Nhap vao tham nien cua nhan vien tinh theo nam: " ))
    luong  =  6000000  *  tn  * ( 5 / 100 )
    return  n , qq , tn , luong
x  =  int ( input ( "Nhap vao so luong nhan vien can nhap thong tin: " ))
lst  = []
for  i  in  range( x ):
    lst . append( nv ())
print ( f"Danh sách thông tin có bản cua { x } nhân viên nhap tu ban phím lan luot tu ten, que quan, tham nien và luong { lst } " )