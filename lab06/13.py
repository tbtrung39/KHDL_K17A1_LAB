# viet chuong trinh
chu_ngu=["Anh","Em"]
dong_tu=["Choi","Yeu"]
tan_ngu=["Bong da","Bong ro"]

cau=[f"{chu} {dong} {tan}" for chu in chu_ngu for dong in dong_tu for tan in tan_ngu]
for cau_don in cau:
    print(cau_don)