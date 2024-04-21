'''
Viết một chương trình để tạo tất cả các câu có chủ ngữ nằm trong ["Anh", "Em"], 
động từ nằm trong ["Chơi", "Yêu") và tân ngữ là ["Bóng đá", "Bóng rổ"].

'''
chu_ngu = ["Anh", "Em"]
dong_tu = ["Chơi", "Yêu"]
tan_ngu = ["Bóng đá", "Bóng rổ"]

# Tạo tất cả các câu
cau = tuple(f"{cn} {dt} {tn}." for cn in chu_ngu for dt in dong_tu for tn in tan_ngu)

# In tất cả các câu đã tạo
print("Tất cả các câu có thể tạo:", cau)