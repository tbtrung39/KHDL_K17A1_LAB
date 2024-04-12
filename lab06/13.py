chu_ngu = ["Anh", "Em"]
dong_tu = ["Choi", "Yeu"]
tan_ngu = ["Bong da", "Bong ro"]
cau = [(S, V, O ) for S in chu_ngu for V in dong_tu for O in tan_ngu]
for cau in cau:
    print(" ".join(cau))