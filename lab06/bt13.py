chu_ngu = ["Anh","Em"]
dong_tu = ["Chơi","Yêu"]
tan_ngu = ["Bóng đá","Bóng rổ"]
cau = []
for i in chu_ngu:
    for j in dong_tu:
        for k in tan_ngu:
            cau.append(i + " " + j + " " + k)
for l in cau:
    print(l)