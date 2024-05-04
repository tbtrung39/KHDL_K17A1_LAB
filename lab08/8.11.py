def  diem_trung_binh ( toan , ly , hoa ):
    diem_trung_binh = ( toan + ly + hoa ) / 3
    return diem_trung_binh
ho_ten  =  input ( "Nhap ho va ten: " )
toan  =  float ( input ( "Nhập điểm toàn: " ))
ly  =  float ( input ( "Nhap diem ly: " ))
hoa  =  float ( input ( "Nhập điểm hoa: " ))
print ( "Hồ va mười: " , ho_ten , "Toan: " , toan , "Ly: " , ly , "Hoa: " , hoa , "Diễm trung bình môn: " , diem_trung_binh ( toan , ly , hoa ))