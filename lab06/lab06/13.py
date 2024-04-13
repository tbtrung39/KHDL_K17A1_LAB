chu_ngu = ["Anh", "Em"]
dong_tu = ["Chơi", "Yêu"]
tan_ngu = ["Bóng đá", "Bóng rổ"]
cau = [(chu_nguu, dong_tuu, tan_nguu) for chu_nguu in chu_ngu for dong_tuu in dong_tu for tan_nguu in tan_ngu]
for cau in cau:
    print(" ".join(cau))
