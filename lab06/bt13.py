chu_ngu = ["Anh", "Em"]
dong_tu = ["Chơi", "Yêu"]
tan_ngu = ["Bóng đá", "Bóng rổ"]

# Tạo tất cả các câu
cau_hoan_chinh = [f"{chu_ngu} {dong_tu} {tan_ngu}" for chungu in chu_ngu for dongtu in dong_tu for tanngu in tan_ngu]

# In tất cả các câu đã tạo
for i in cau_hoan_chinh:
    print(i)
